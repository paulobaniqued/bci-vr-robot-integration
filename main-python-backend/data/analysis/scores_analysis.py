#%%
""" Import Data """
import numpy as np
import pandas as pd

imported_data =  pd.read_csv('E:\\bci\\data\\test\\scores-test.csv')
print(imported_data)

# %%
""" Repeated Measures ANOVA """
from statsmodels.stats.anova import AnovaRM

print(AnovaRM(data=imported_data, depvar='score', subject='condition', within=['day']).fit())

# Ha : p-value < 0.05
# Reporting : statistically significant (F(3,9) = 11.4315, p = 0.0020)


# %%
""" Linear Regression Analysis """
from sklearn.linear_model import LinearRegression

def get_coef(data, condition):
    df = data[data['condition'] == condition]
    lr = LinearRegression()
    lr.fit(df[['score']], df['day'])
    slope = lr.coef_
    return slope

lr_1 = get_coef(imported_data, 1)
lr_2 = get_coef(imported_data, 2)
lr_3 = get_coef(imported_data, 3)
lr_4 = get_coef(imported_data, 4)
print(lr_1, lr_2, lr_3, lr_4)

# %%
""" Plot Data """
import matplotlib.pyplot as plt
import seaborn as sns

sns.lmplot(x="day", y="score", hue="condition", data=imported_data)
plt.xlabel("Sessions")
plt.ylabel("Online Accuracy (%)")
plt.xticks([1,2,3,4,5,6,7,8])
plt.show()

# %%
