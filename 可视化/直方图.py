import pandas as pd
import matplotlib.pyplot as plt

# 读数据
data = pd.read_csv('../today_province_2022_06_16.csv')
# 画直方图
plt.rcParams['font.sans-serif'] = ['SimHei']
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 8))
d = 5000  # 组距
x = data.total_heal
num_bins = (max(x) - min(x)) // d
ax.hist(x, bins=num_bins)
# 设置x轴刻度
plt.xticks(range(min(x), max(x) + d, d))
plt.title('总治愈人数的分布直方图')
plt.savefig('直方图.svg', dpi=600)
plt.show()
