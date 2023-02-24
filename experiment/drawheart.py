import numpy as np
import matplotlib.pyplot as plt

# ハートのグラフを描画するためのxの値を作成
t = np.linspace(0, 2*np.pi, 1000)
x = 16*np.sin(t)**3
y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)

# グラフを描画
fig, ax = plt.subplots()
ax.plot(x, y, color='red')

# グラフの設定
ax.set_aspect('equal')
ax.set_title('Heart')
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.show()
