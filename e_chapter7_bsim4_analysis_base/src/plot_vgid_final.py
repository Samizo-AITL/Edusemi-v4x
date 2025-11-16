import numpy as np
import matplotlib.pyplot as plt
import matplotlib

print("Matplotlib backend:", matplotlib.get_backend())

# === 1. NMOS / PMOS のログを読む ===
n = np.loadtxt("vgid_nmos.log")
p = np.loadtxt("vgid_pmos.log")

print("NMOS shape:", n.shape)
print("PMOS shape:", p.shape)
print("NMOS first row:", n[0, :])
print("NMOS last  row:", n[-1, :])

# ログ形式: [Vg, Vg, Vg, Id]
vg_n = n[:, 0]
id_n = np.abs(n[:, 3])   # 4列目が Id

vg_p = p[:, 0]
id_p = np.abs(p[:, 3])   # 4列目が Id

# === 2. 線形スケールの Id–Vg を PNG に保存 ===
fig1, ax1 = plt.subplots(figsize=(7, 5))
ax1.plot(vg_n, id_n * 1e6, ".", label="nMOS")
ax1.plot(vg_p, id_p * 1e6, ".", label="pMOS")
ax1.set_xlabel("Vg [V]")
ax1.set_ylabel("Id [µA]")
ax1.set_title("Vg–Id (using 4th column as Id)")
ax1.grid(True)
ax1.legend()
fig1.tight_layout()
fig1.savefig("vgid_linear.png")
print("Saved: vgid_linear.png")

# === 3. y軸ログの Id–Vg を PNG に保存 ===
fig2, ax2 = plt.subplots(figsize=(7, 5))
ax2.semilogy(vg_n, id_n, ".", label="nMOS")
ax2.semilogy(vg_p, id_p, ".", label="pMOS")
ax2.set_xlabel("Vg [V]")
ax2.set_ylabel("Id [A]")
ax2.set_title("Vg–Id (log scale, 4th column)")
ax2.grid(True, which="both")
ax2.legend()
fig2.tight_layout()
fig2.savefig("vgid_log.png")
print("Saved: vgid_log.png")

# ウィンドウは出さない
# plt.show()
