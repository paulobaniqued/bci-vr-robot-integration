# %%
""" Import Data """
import numpy as np
import pandas as pd
from statistics import mean, stdev
import matplotlib.pyplot as plt
import seaborn as sns

sesh_per_cond = 4
cond = ['a', 'b', 'c', 'd']
results_columns = ['condition', 'session', 'score']
results = pd.DataFrame(columns = results_columns)
means_columns = ['condition', 'mean_score', 'stdev']
means = pd.DataFrame(columns = means_columns)

for condition in cond:
    sesh_count = 1
    cond_scores = []

    for sesh in range(sesh_per_cond):
        file_code = condition + str(sesh_count)
        imported_score = pd.read_csv('E:\\bci\\data\\analysis\\csv\\{}.csv'.format(file_code))
        score = max(imported_score['score'])
        trials = max(imported_score['trial'])
        acc = round((score/trials)*100, 2)
        results_entry = pd.DataFrame([[condition, float(sesh_count), acc]], columns = results_columns)
        results = results.append(results_entry, ignore_index = True)

        cond_scores.append(acc)

        sesh_count += 1
    
        if sesh_count == 4:
            cond_mean = mean(cond_scores)
            cond_sd = stdev(cond_scores)
            means_entry = pd.DataFrame([[condition, cond_mean, cond_sd]], columns = means_columns)
            means = means.append(means_entry, ignore_index = True)

print(results)
print(means)

""" Plot Mean Scores """
sns.catplot(
    data = results, kind="bar",
    x="condition", y="score", ci="sd"
)

# %%
""" Repeated Measures ANOVA """
from statsmodels.stats.anova import AnovaRM

print(AnovaRM(data=imported_data, depvar='score', subject='condition', within=['session']).fit())

# Ha : p-value < 0.05
# Reporting : statistically significant (F(3,9) = 11.4315, p = 0.0020)

# %%
""" Linear Regression Analysis """
from sklearn.linear_model import LinearRegression

def get_coef(data, condition):
    df = data[data['condition'] == condition]
    lr = LinearRegression()
    lr.fit(df[['score']], df['session'])
    slope = lr.coef_
    return slope

lr_1 = get_coef(results, 'a')
lr_2 = get_coef(results, 'b')
lr_3 = get_coef(results, 'c')
lr_4 = get_coef(results, 'd')
print("Linear Coefficients for A, B, C, D: ")
print(lr_1, lr_2, lr_3, lr_4)

""" Plot Linear Regression Analysis """
sns.lmplot(x='session', y='score', hue='condition', data=results)
plt.xlabel("Sessions")
plt.ylabel("Online Accuracy (%)")
plt.xticks([1,2,3,4])
plt.yticks([10,20,30,40,50,60,70,80,90,100])
plt.ylim(20,100)
plt.show()

# %%

# %%
