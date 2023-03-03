import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Import Data
df = pd.read_csv("DATA.csv")

# Prepare Data
x = df['date'].values.tolist()
y1 = df['A'].values.tolist()
y2 = df['B'].values.tolist()
y3 = df['C'].values.tolist()
y4 = df['D'].values.tolist()
mycolors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:brown', 'tab:grey', 'tab:pink', 'tab:olive']
columns = ['A','B', 'C','D']

# Draw Plot
fig, ax = plt.subplots(1, 1, figsize=(16,9), dpi= 80)
ax.fill_between(x, y1=y1, y2=0, label=columns[0], alpha=0.5, color=mycolors[1], linewidth=2)
ax.fill_between(x, y1=y2, y2=0, label=columns[1], alpha=0.5, color=mycolors[0], linewidth=2)
ax.fill_between(x, y1=y3, y2=0, label=columns[2], alpha=0.5, color=mycolors[3], linewidth=2)
ax.fill_between(x, y1=y4, y2=0, label=columns[3], alpha=0.5, color=mycolors[6], linewidth=2)
# Decorations
ax.set_title('A vs B vs C vs D', fontsize=18)
ax.set(ylim=[0, 30])
ax.legend(loc='best', fontsize=12)
plt.xticks(x[::50], fontsize=10, horizontalalignment='center')
plt.yticks(np.arange(2.5, 30.0, 2.5), fontsize=10)
plt.xlim(-10, x[-1])

# Draw Tick lines
for y in np.arange(2.5, 30.0, 2.5):
    plt.hlines(y, xmin=0, xmax=len(x), colors='black', alpha=0.3, linestyles="--", lw=0.5)

# Lighten borders
plt.gca().spines["top"].set_alpha(0)
plt.gca().spines["bottom"].set_alpha(.3)
plt.gca().spines["right"].set_alpha(0)
plt.gca().spines["left"].set_alpha(.3)
plt.show()

