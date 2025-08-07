# tddb_model.py

import numpy as np
import os
from common_plot import setup_plot, finalize_plot

# パラメータ
E = np.linspace(4, 10, 200)  # 電界強度 [MV/cm]
gamma = 30  # モデル定数
A = 1e-6    # スケール定数 [秒]

# TDDB モデル式（E-model）
lifetime = A * np.exp(gamma / E)

# グラフ描画
os.makedirs("figures", exist_ok=True)
setup_plot("TDDB Lifetime vs Electric Field", "Electric Field [MV/cm]", "Lifetime [s]")
plt.plot(E, lifetime)
plt.yscale("log")
finalize_plot("figures/tddb_lifetime_plot.png")
