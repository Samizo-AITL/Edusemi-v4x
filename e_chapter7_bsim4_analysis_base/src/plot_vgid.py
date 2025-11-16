from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


# =========================================================
#  パス設定：プロジェクトルートから決め打ち
# =========================================================
ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw"
FIG_DIR = ROOT / "figs"
FIG_DIR.mkdir(exist_ok=True)


# ---------------------------------------------------------
#  ログ読み込み
#   形式: Vg, ..., ..., Id
# ---------------------------------------------------------
def load_vg_id(path: Path):
    data = np.loadtxt(path)
    vg = data[:, 0]
    id_abs = np.abs(data[:, -1])
    # Vg昇順にソート
    idx = np.argsort(vg)
    return vg[idx], id_abs[idx]


# ---------------------------------------------------------
#  sqrt(Id)–Vg 線形フィットで Vth を抽出
# ---------------------------------------------------------
def extract_vth_sqrt(vg, id_abs, id_min=1e-8, id_max=1e-5):
    y = np.sqrt(id_abs)
    mask = (id_abs >= id_min) & (id_abs <= id_max)
    if mask.sum() < 2:
        raise RuntimeError("Vth抽出用のデータ点が足りません。id_min/id_max を調整してください。")
    vg_fit = vg[mask]
    y_fit = y[mask]
    a, b = np.polyfit(vg_fit, y_fit, 1)
    vth = -b / a
    return vth, (a, b), vg_fit, y_fit


def main():
    n_low_log = RAW_DIR / "vgid_nmos_vd05.log"
    p_low_log = RAW_DIR / "vgid_pmos_vd05.log"

    print(f"Loading logs from: {RAW_DIR}")
    vg_n, id_n = load_vg_id(n_low_log)
    vg_p, id_p = load_vg_id(p_low_log)

    print(f"nMOS log: {n_low_log}, shape={vg_n.shape}, "
          f"Vg[min,max]=({vg_n.min():.2f},{vg_n.max():.2f}), "
          f"|Id|[min,max]=({id_n.min():.3e},{id_n.max():.3e})")
    print(f"pMOS log: {p_low_log}, shape={vg_p.shape}, "
          f"Vg[min,max]=({vg_p.min():.2f},{vg_p.max():.2f}), "
          f"|Id|[min,max]=({id_p.min():.3e},{id_p.max():.3e})")

    # ----- Vth 抽出 -----
    vth_n, (a_n, b_n), vg_n_fit, y_n_fit = extract_vth_sqrt(vg_n, id_n)
    vth_p, (a_p, b_p), vg_p_fit, y_p_fit = extract_vth_sqrt(vg_p, id_p)

    print("")
    print(f"nMOS Vth = {vth_n:+.3f} V")
    print(f"pMOS Vth = {vth_p:+.3f} V")

    # =====================================================
    #  プロット
    # =====================================================
    fig, axes = plt.subplots(1, 3, figsize=(12, 3))

    # ---- 1) Id–Vg (linear) ----
    ax = axes[0]
    ax.plot(vg_n, id_n * 1e6, ".", label="nMOS")
    ax.plot(vg_p, id_p * 1e6, ".", label="pMOS")
    ax.set_xlabel("Vg [V]")
    ax.set_ylabel("Id [µA]")
    ax.set_title("Id–Vg (linear)")
    ax.grid(True)
    ax.legend()

    # ---- 2) Id–Vg (log) ----
    ax = axes[1]
    ax.semilogy(vg_n, id_n, ".", label="nMOS")
    ax.semilogy(vg_p, id_p, ".", label="pMOS")
    ax.set_xlabel("Vg [V]")
    ax.set_ylabel("Id [A]")
    ax.set_title("Id–Vg (log scale)")
    ax.grid(True, which="both")
    ax.legend()

    # ---- 3) sqrt(Id)–Vg & Vth ----
    ax = axes[2]
    ax.plot(vg_n, np.sqrt(id_n), ".", label="nMOS data")
    ax.plot(vg_p, np.sqrt(id_p), ".", label="pMOS data")

    vg_n_line = np.linspace(vg_n_fit.min(), vg_n_fit.max(), 100)
    vg_p_line = np.linspace(vg_p_fit.min(), vg_p_fit.max(), 100)
    ax.plot(vg_n_line, a_n * vg_n_line + b_n, "g--", label="nMOS fit")
    ax.plot(vg_p_line, a_p * vg_p_line + b_p, "r--", label="pMOS fit")

    ax.axvline(vth_n, ls="--", color="g", label=f"Vth_n={vth_n:+.3f}V")
    ax.axvline(vth_p, ls="--", color="r", label=f"Vth_p={vth_p:+.3f}V")

    ax.set_xlabel("Vg [V]")
    ax.set_ylabel("sqrt(Id) [A^0.5]")
    ax.set_title("sqrt(Id)–Vg & Vth")
    ax.grid(True)
    ax.legend()

    plt.tight_layout()

    out_path = FIG_DIR / "vgid_all.png"
    plt.savefig(out_path, dpi=150)
    print(f"\nSaved figure to: {out_path}")

    # 画面にも出したければコメント解除
    # plt.show()


if __name__ == "__main__":
    main()
