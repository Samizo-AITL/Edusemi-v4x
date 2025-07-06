import numpy as np
import matplotlib.pyplot as plt

# 電界範囲 [MV/cm]
E = np.linspace(2, 10, 300)  # 実用領域

# フィールドパワーモデル（n = 2, 3, 4）
n_values = [2, 3, 4]
for n in n_values:
    mttf_fp = 1 / (E ** n)
    plt.plot(E, mttf_fp, label=f"Power Model n={n}", linestyle="--")

# Eモデル（γ = -2, -3）
gamma_values = [-2, -3]
for gamma in gamma_values:
    mttf_exp = np.exp(gamma * E)
    plt.plot(E, mttf_exp, label=f"E-Model γ={gamma}")

plt.yscale("log")
plt.xlabel("酸化膜電界 E [MV/cm]")
plt.ylabel("MTTF (任意単位, log表示)")
plt.title("TDDBモデル比較：MTTF vs 電界E")
plt.grid(True, which="both", linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig("output/tddb_models.png")
plt.show()
