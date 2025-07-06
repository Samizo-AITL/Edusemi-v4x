import numpy as np
import matplotlib.pyplot as plt

# 定数（簡易モデル）
k = 8.617e-5  # eV/K
Ea = 0.15     # 活性化エネルギー [eV]
A = 1e-3      # スケーリング定数
n = 0.2       # 時間依存係数

# 温度条件（25°C, 85°C, 125°C）
temperatures = [298, 358, 398]  # [K]
labels = ["25°C", "85°C", "125°C"]

# 時間軸（10秒〜10^7秒）
t = np.logspace(1, 7, 300)  # 秒

# プロット
plt.figure(figsize=(8, 5))
for T, label in zip(temperatures, labels):
    delta_vth = A * (t ** n) * np.exp(-Ea / (k * T))
    plt.plot(t, delta_vth, label=f"T = {label}")

plt.xscale("log")
plt.xlabel("Stress Time t [s]")
plt.ylabel("ΔVth [V]")
plt.title("BTI劣化モデル：ΔVth vs 時間")
plt.grid(True, which="both", linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig("output/bti_degradation.png")
plt.show()
