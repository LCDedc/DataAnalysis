import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读数据
data = pd.read_csv('../today_province_2022_06_16.csv')
plt.rcParams['font.sans-serif'] = ['SimHei']
# 画相关散点图
cols = ['total_confirm', 'total_heal', 'total_dead']
sns.pairplot(data[cols], size=2.5)
plt.tight_layout()
plt.savefig('散点图.svg', dpi=600)
plt.show()
