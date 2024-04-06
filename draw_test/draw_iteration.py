import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import numpy as np


plt.rc('font',family='Times New Roman')

iters = [i * 100 for i in range(1, 30 + 1)]
a = np.array(
     [0.01, 0.06, 0.12, 0.18, 0.27, 0.30, 0.37, 0.42, 0.45, 0.46,
      0.47, 0.60, 0.53, 0.55, 0.56, 0.63, 0.86, 0.68, 0.63, 0.71,
      0.78, 0.78, 0.79, 0.78, 0.79, 0.79, 0.78, 0.77, 0.77, 0.78])
a = savgol_filter(a, 9, 1)
b = np.array(
     [0.02, 0.14, 0.27, 0.36, 0.44, 0.71, 0.72, 0.62, 0.64, 0.83,
      0.76, 0.72, 0.84, 0.79, 0.81, 0.66, 0.73, 0.79, 0.90, 0.85,
      0.85, 0.86, 0.85, 0.85, 0.86, 0.85, 0.86, 0.85, 0.85, 0.86])
b = savgol_filter(b, 9, 1)
c = np.array(
     [0.04, 0.18, 0.33, 0.45, 0.68, 0.60, 0.77, 0.55, 0.58, 0.61,
      0.67, 0.59, 0.76, 0.91, 0.74, 0.67, 0.92, 0.75, 0.66, 0.75,
      0.75, 0.76, 0.75, 0.75, 0.75, 0.76, 0.76, 0.75, 0.76, 0.75])
c = savgol_filter(c, 9, 1)

plt.plot(iters, a, 's-', linewidth=2.0, color='blue')
plt.plot(iters, b, 'o-', linewidth=2.0, color='black')
plt.plot(iters, c, '^-', linewidth=2.0, color='red')

plt.grid(axis="x", linestyle='--')
plt.grid(axis="y", linestyle='--')

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Training iteration', fontsize=16)
plt.ylabel('Average Precision', fontsize=16)
labels = ['lr=0.001', 'lr=0.005', 'lr=0.01']
plt.legend(labels, loc='lower right', fontsize=16)
plt.show()

