import pandas as pd
import matplotlib.pyplot as plt

# 读数据
data = pd.read_csv('../today_province_2022_06_16.csv')
data = data.sort_values('total_confirm', ascending=False)  # 按照总的确诊人数排序
pie_data = list(data['total_confirm'][:5])  # 画出前五的
pie_data.append(data['total_confirm'][5:].sum())
pie_index = list(data['name'][:5])
pie_index.append('其他省市')
# 画饼图
plt.rcParams['font.sans-serif'] = ['SimHei']
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 8))
ax.pie(pie_data, autopct='%1.1f%%', labels=pie_index)
ax.set_title('总确诊人数的比例图')
plt.savefig('饼图.svg', dpi=600)
plt.show()
