import numpy as np
import matplotlib.pyplot as plt

# x軸の範囲を設定
x = np.linspace(-1, 1, 500)

# y軸の範囲を設定
y1 = np.sqrt(1 - (np.abs(x) - 1) ** 2)
y2 = -3 * np.sqrt(1 - (np.abs(x) / 2) ** 0.5)

# グラフを描画
plt.fill_between(x, y1, color='red', alpha=0.5)
plt.fill_between(x, y2, color='red', alpha=0.5)

# グラフの装飾
plt.axis('off')
plt.show()