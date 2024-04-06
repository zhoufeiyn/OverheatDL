import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import numpy as np

plt.rc('font',family='Times New Roman')
nr_anchors = np.array([1, 3, 5, 7])
a = np.array([0.8, 0.91, 0.92, 0.90])
plt.plot(nr_anchors, a, 's-', linewidth=2.0, color='blue')

plt.grid(axis="x", linestyle='--')
plt.grid(axis="y", linestyle='--')

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Number of Anchor', fontsize=16)
plt.ylabel('Average Precision', fontsize=16)

plt.show()
