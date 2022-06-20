#读取数据
path="data/"
n=0
with open(path+'b.txt','r') as f:
    num_all=dict()
    b=f.readlines()
    with open(path+'a.txt') as f:
        a=f.readlines()

        for b_ in b:
            num=0
            bb=set(b_[:-1].split(','))
            for a_ in a:
                aa=set(a_[:-1].split(','))#变成集合
                set_num=len(aa&bb)
                if set_num==5:
                    num+=1

            num_all[b_[:-1]]=num
            n+=1
            print("已比较{}组数据".format(n))

#将结果存入txt文件
num_all=dict(sorted(num_all.items(),key=lambda x:x[1]))
with open(path+'结果.txt','w') as f:
    for items in num_all.items():
        f.write("{}交集 5 次数{}\n".format(items[0],items[1]))