import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 读数据
data = pd.read_csv('../today_province_2022_06_16.csv')
plt.rcParams['font.sans-serif'] = ['SimHei']
# 绘制相关系数的热图

cols = ['total_confirm', 'total_heal', 'total_dead']
cm = np.corrcoef(data[cols].values.T)
# sns.set(font_scale=1.5)
hm = sns.heatmap(cm,
                 cbar=True,
                 annot=True,
                 square=True,
                 fmt='.2f',
                 annot_kws={'size': 15},
                 yticklabels=cols,
                 xticklabels=cols)

plt.tight_layout()
plt.title('总确诊、总治愈、总死亡之间的相关系数热图')
plt.savefig('热图.svg', dpi=600)
plt.show()
