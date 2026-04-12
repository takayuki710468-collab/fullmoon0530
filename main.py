
import numpy as np
import matplotlib.pyplot as plt

# 距離
r = np.linspace(0.1, 1.0, 200)

# 構造対応（レンジベース）
def structure_value(r):
    F = []

    for x in r:
        if x < 0.3:
            # 内側（ほぼ未補正）
            value = 3.0
        elif 0.3 <= x < 0.6:
            # 中距離（立ち上がり）
            value = 3.0 + (3.5 - 3.0) * (x - 0.3) / (0.6 - 0.3)
        else:
            # 外側（飽和）
            value = 5.5

        F.append(value)

    return np.array(F)

F = structure_value(r)

# 可視化
plt.plot(r, F)
plt.xlabel("Distance")
plt.ylabel("Structure Value")
plt.title("Structure Mapping (Phase-based)")
plt.grid()

plt.show()