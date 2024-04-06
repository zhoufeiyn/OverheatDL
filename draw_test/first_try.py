import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import numpy as np

plt.rc('font',family='Times New Roman')
def draw_loss():
    iters = [(i+1) * 264  for i in range(12)]
    # a = np.array(
    #      [0.01, 0.06, 0.12, 0.18, 0.27, 0.30, 0.37, 0.42, 0.45, 0.46,
    #       0.47, 0.60, 0.53, 0.55, 0.56, 0.63, 0.86, 0.68, 0.63, 0.71,
    #       0.78, 0.78, 0.79, 0.78, 0.79, 0.79, 0.78, 0.77, 0.77, 0.78])
    # a = savgol_filter(a, 9, 1)
    b=np.array([0.8011,	0.4918,	0.4313,	0.4163,	0.4659,
    0.4453,	0.4339,	0.3505,	0.3696,	0.4537,
    0.3536,	0.3614,	0.3615,	0.3323,	0.3533,
    0.3154,	0.2969,	0.2957,	0.2845,	0.2848,
    0.3292,	0.2621,	0.2837,	0.2551,	0.2349,
    0.2487,	0.2553,	0.2549,	0.2546,	0.2592,
    0.2172,	0.2109,	0.2161,	0.2458,	0.2307,
    0.2099,	0.2251,	0.2064,	0.2035,	0.2416,
    0.1857,	0.161,  0.1828,	0.1484,	0.1619,
    0.1471,	0.1774,	0.1691, 0.147,	0.1673,
    0.1665,	0.1455,	0.1506,	0.1593,	0.1522,
    0.1397,	0.1461,	0.1484,	0.1706,	0.1529])

    b = savgol_filter(b, 9, 1)
    # c = np.array(
    #      [0.04, 0.18, 0.33, 0.45, 0.68, 0.60, 0.77, 0.55, 0.58, 0.61,
    #       0.67, 0.59, 0.76, 0.91, 0.74, 0.67, 0.92, 0.75, 0.66, 0.75,
    #       0.75, 0.76, 0.75, 0.75, 0.75, 0.76, 0.76, 0.75, 0.76, 0.75])
    # c = savgol_filter(c, 9, 1)

    # plt.plot(iters, a, 's-', linewidth=2.0, color='blue')
    plt.plot(iters, b[::5], 'o-', linewidth=2.0, color='blue')
    # plt.plot(iters, c, '^-', linewidth=2.0, color='red')

    plt.grid(axis="x", linestyle='--')
    plt.grid(axis="y", linestyle='--')

    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.xlabel('Iteration', fontsize=16)
    plt.ylabel('Loss', fontsize=16)
    # labels = ['lr=0.001', 'lr=0.005', 'lr=0.01']
    # plt.legend(labels, loc='lower right', fontsize=16)
    plt.show()


def draw_ap():
    iters = [(i + 1) * 264 for i in range(12)]
    b=[0.039,0.206,0.319,0.579,0.773,0.61,0.656,0.662,0.877,0.88,0.877,0.871]

    b = savgol_filter(b, 9, 1)
    # c = np.array(
    #      [0.04, 0.18, 0.33, 0.45, 0.68, 0.60, 0.77, 0.55, 0.58, 0.61,
    #       0.67, 0.59, 0.76, 0.91, 0.74, 0.67, 0.92, 0.75, 0.66, 0.75,
    #       0.75, 0.76, 0.75, 0.75, 0.75, 0.76, 0.76, 0.75, 0.76, 0.75])
    # c = savgol_filter(c, 9, 1)

    # plt.plot(iters, a, 's-', linewidth=2.0, color='blue')
    plt.plot(iters, b, 'o-', linewidth=2.0, color='blue')
    # plt.plot(iters, c, '^-', linewidth=2.0, color='red')

    plt.grid(axis="x", linestyle='--')
    plt.grid(axis="y", linestyle='--')

    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.xlabel('Iteration', fontsize=16)
    plt.ylabel('Average Precision', fontsize=16)
    # labels = ['lr=0.001', 'lr=0.005', 'lr=0.01']
    # plt.legend(labels, loc='lower right', fontsize=16)
    plt.show()


if __name__ == "__main__":
    draw_loss()
    # draw_ap()