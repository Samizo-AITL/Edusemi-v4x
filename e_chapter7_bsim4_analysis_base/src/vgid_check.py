import numpy as np
import matplotlib.pyplot as plt

# ---- 1. NMOS ログを読む ----
n_data = np.loadtxt("vgid_nmos.log")
print("NMOS shape:", n_data.shape)
print("NMOS first row:", n_data[0, :])
print("NMOS last  row:", n_data[-1, :])

# 列の中身をバラしてみる
vg0 = n_data[:, 0]
vg1 = n_data[:, 1]
vg2 = n_data[:, 2]
id4 = n_data[:, 3]   # ★ ここが本物の Id だったはず

# ---- 2. 「どの列が何を表しているか」目視確認用 グラフ ----
fig, ax = plt.subplots(2, 2, figsize=(10, 8))

ax[0, 0].plot(vg0, label="col0 (x)")
ax[0, 0].set_title("NMOS col0 vs index")
ax[0, 0].grid(True)

ax[0, 1].plot(vg0, vg1, ".", label="col1")
ax[0, 1].set_title("NMOS Vg (col0) vs col1")
ax[0, 1].grid(True)

ax[1, 0].plot(vg0, vg2, ".", label="col2")
ax[1, 0].set_title("NMOS Vg (col0) vs col2")
ax[1, 0].grid(True)

ax[1, 1].plot(vg0, id4, ".", label="col3 = Id?")
ax[1, 1].set_title("NMOS Vg (col0) vs col3")
ax[1, 1].set_xlabel("Vg [V]")
ax[1, 1].set_ylabel("value")
ax[1, 1].grid(True)

plt.tight_layout()
plt.show()


# ---- 3. MOSFET らしい Vg-Id のみ描画 ----
#    4列目(col3)を Id とみなして Vg-Id を描く

vg = vg0
Id = id4

fig2, ax2 = plt.subplots(figsize=(6, 4))
ax2.plot(vg, np.abs(Id), ".-")
ax2.set_xlabel("Vg [V]")
ax2.set_ylabel("Id [A]")
ax2.set_title("NMOS Id–Vg (using col3 as Id)")
ax2.grid(True)
plt.show()
