import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读数据
data = pd.read_csv('../today_province_2022_06_16.csv')
plt.rcParams['font.sans-serif'] = ['SimHei']
box_data = pd.DataFrame(pd.concat([data.total_heal, data.total_dead]))
tye = []
for s in [['总治愈人数'] * 34, ['总死亡人数'] * 34]:
    for s1 in s:
        tye.append(s1)
box_data['类别'] = tye
box_data.columns = ['人数', '类别']
# 设置绘图风格
plt.style.use('ggplot')
sns.boxplot(x='类别', y='人数', data=box_data, showmeans=True)
plt.title('总治愈人数、总死亡人数的箱线图')
plt.savefig('箱线图.svg')
plt.show()
