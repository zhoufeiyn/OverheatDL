import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import numpy as np

plt.rc('font',family='Times New Roman')
nr_anchors = np.array([400, 600, 800])
a = np.array([0.79, 0.92, 0.91])
b = np.array([0.93, 0.93, 0.93])
plt.plot(nr_anchors, a, 's-', linewidth=2.0, color='blue')
plt.plot(nr_anchors, b, '--', linewidth=2.0, color='blue')
plt.grid(axis="x", linestyle='--')
plt.grid(axis="y", linestyle='--')



plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Image Scale', fontsize=16)
plt.ylabel('Average Precision', fontsize=16)

labels = ['Single-scale','Multiscale']
plt.legend(labels, loc='lower right', fontsize=16)

plt.show()
