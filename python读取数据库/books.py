import requests
from pyquery import PyQuery
import time
import pandas as pd
import pymysql
from sqlalchemy import create_engine


class DDSpider(object):
    def __init__(self, key):
        self.key = key  # 当前搜索的图书名，搜索关键词
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
        }
        self.base_url = 'https://search.dangdang.com/?key=' + key + '&act=input&page_index={}'

    # 获取界面
    def get_pageInfo(self):
        num_page = 0
        while True:
            num_page += 1
            page_url = self.base_url.format(num_page)
            res = requests.get(page_url, headers=self.headers)
            #             print(res.content.decode('GBK'))
            # 解析
            df = self.parse_pageInfo(res.content.decode('gb18030', 'ignore'))
            return df
            time.sleep(1)  # 为了防止请求过快，添加缓冲时间
            if num_page == 1:  # 当前设置为爬取1页数据
                break

    # 解析界面
    def parse_pageInfo(self, html):
        doc = PyQuery(html)
        book_ul = doc('#component_59 li').items()

        img_list = []
        title_list = []
        price_list = []
        comments_list = []
        stars_list = []
        for one_li in book_ul:
            #             print(one_li)
            # 获取图片链接
            if one_li('.pic img').attr('data-original'):
                img_url = one_li('.pic img').attr('data-original')
            else:
                img_url = one_li('.pic img').attr('src')
            img_list.append('http:' + img_url)
            # 标题
            title = one_li('.name a').attr('title')
            #             print(title)
            title_list.append(title)
            # 价格
            price = one_li('.price .search_now_price').text()
            #             print(price)
            price_list.append(price)
            # 获取评价数
            comments = one_li('.search_star_line .search_comment_num').text()
            #             print(comments)
            comments_list.append(comments)
            # 获取星数
            stars = float(one_li('.search_star_black span').attr('style').split(':')[-1].strip('%;')) / 20
            # stars = one_li('.search_star_black span').attr('style')
            # print(stars)
            stars_list.append(stars)
        data = {'img': img_list, 'title': title_list, 'price': price_list, 'comments': comments_list,
                'stars': stars_list}
        return pd.DataFrame(data)


def connect_mysql():
    db = pymysql.connect(host='localhost', user='root', passwd='198024', db='hrs', port=3306, charset='utf8')
    cursor = db.cursor()
    db_engine = create_engine('mysql+pymysql://root:123456@39.105.11.250/analysis')
    db_connection = db_engine.connect()
    return db, cursor, db_engine, db_connection


def execute_mysql_script(script):
    db, cursor, db_engine, db_connection = connect_mysql()
    cursor.execute(script)
    cursor.close()


if __name__ == '__main__':
    dd = DDSpider('python')
    df = dd.get_pageInfo()
    # 数据存入数据库
    db, cursor, db_engine, db_connection = connect_mysql()
    table_name = 'books'
    script = f'''
    CREATE TABLE {table_name} (
      img CHAR(255) NOT NULL,
      title CHAR(255)NOT NULL,
      price CHAR(255)NOT NULL,
      comments CHAR(255)NOT NULL,
      stars INT NOT NULL
      )'''

    #### 当表名存在时，在这里我跳过错误 ####
    try:
        execute_mysql_script(script)
    except:
        pass
    # 存入数据库
    df.to_sql(table_name, con=db_engine, if_exists='append', index=False)
