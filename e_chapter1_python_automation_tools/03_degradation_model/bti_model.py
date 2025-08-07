# bti_model.py

import numpy as np
import os
from common_plot import setup_plot, finalize_plot

# 定数定義
k = 8.617e-5  # Boltzmann定数 [eV/K]
Ea = 0.45     # 活性化エネルギー [eV]
n = 0.25      # 時間指数
T = 373       # 温度 [K] (例：100°C)
t = np.logspace(1, 5, 200)  # 時間 [秒]

# ΔVth モデル式
delta_vth = 50e-3 * (t**n) * np.exp(-Ea / (k * T))  # 単位: V

# グラフ描画
os.makedirs("figures", exist_ok=True)
setup_plot("BTI Vth Shift Over Time", "Time [s]", "ΔVth [V]")
plt.plot(t, delta_vth, label=f"T = {T-273}°C")
plt.xscale("log")
plt.legend()
finalize_plot("figures/bti_vth_shift.png")
