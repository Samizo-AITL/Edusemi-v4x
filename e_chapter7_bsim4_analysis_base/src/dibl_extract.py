from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw"
FIG_DIR = ROOT / "figs"
FIG_DIR.mkdir(exist_ok=True)


def load_vg_id(path: Path):
    data = np.loadtxt(path)
    vg = data[:, 0]
    id_abs = np.abs(data[:, -1])
    # とりあえず昇順で揃えておく
    idx = np.argsort(vg)
    return vg[idx], id_abs[idx]


def extract_vth_const_id(vg, id_abs, iref, pmos=False):
    """
    const-Id 法で Vth を求める。
    pMOS=True のときは Vg を 0V 側から負方向へ見ていくイメージで探索。
    """
    id_min = id_abs.min()
    id_max = id_abs.max()
    if not (id_min <= iref <= id_max):
        raise RuntimeError(
            f"Iref={iref:.2e} A が Id 範囲 [{id_min:.2e}, {id_max:.2e}] に入っていません。"
        )

    # 並び替え（pMOS のときは Vg を降順にして 0→負方向へ）
    if pmos:
        order = np.argsort(vg)[::-1]  # Vg: 0, -0.01, ..., -1.2
    else:
        order = np.argsort(vg)        # Vg: 0, 0.01, ..., 1.2

    vg_use = vg[order]
    id_use = id_abs[order]

    idx = np.where(id_use >= iref)[0]
    if len(idx) == 0:
        k = np.argmin(np.abs(id_use - iref))
        return vg_use[k]

    k = idx[0]
    if k == 0:
        return vg_use[0]

    v1, v2 = vg_use[k - 1], vg_use[k]
    i1, i2 = id_use[k - 1], id_use[k]
    slope = (i2 - i1) / (v2 - v1)
    vth = v1 + (iref - i1) / slope
    return vth


def main():
    NMOS_LOG_LOW = RAW_DIR / "vgid_nmos_vd05.log"
    NMOS_LOG_HIGH = RAW_DIR / "vgid_nmos.log"
    PMOS_LOG_LOW = RAW_DIR / "vgid_pmos_vd05.log"
    PMOS_LOG_HIGH = RAW_DIR / "vgid_pmos.log"

    print(f"Loading logs from: {RAW_DIR}")
    vg_n_low, id_n_low = load_vg_id(NMOS_LOG_LOW)
    vg_n_high, id_n_high = load_vg_id(NMOS_LOG_HIGH)
    vg_p_low, id_p_low = load_vg_id(PMOS_LOG_LOW)
    vg_p_high, id_p_high = load_vg_id(PMOS_LOG_HIGH)

    print(f"{NMOS_LOG_LOW.name}: shape={vg_n_low.shape}, "
          f"Vg[min,max]=({vg_n_low.min():.2f},{vg_n_low.max():.2f}), "
          f"|Id|[min,max]=({id_n_low.min():.3e},{id_n_low.max():.3e})")
    print(f"{NMOS_LOG_HIGH.name}: shape={vg_n_high.shape}, "
          f"Vg[min,max]=({vg_n_high.min():.2f},{vg_n_high.max():.2f}), "
          f"|Id|[min,max]=({id_n_high.min():.3e},{id_n_high.max():.3e})")
    print(f"{PMOS_LOG_LOW.name}: shape={vg_p_low.shape}, "
          f"Vg[min,max]=({vg_p_low.min():.2f},{vg_p_low.max():.2f}), "
          f"|Id|[min,max]=({id_p_low.min():.3e},{id_p_low.max():.3e})")
    print(f"{PMOS_LOG_HIGH.name}: shape={vg_p_high.shape}, "
          f"Vg[min,max]=({vg_p_high.min():.2f},{vg_p_high.max():.2f}), "
          f"|Id|[min,max]=({id_p_high.min():.3e},{id_p_high.max():.3e})")

    IREF = 1.0e-7  # [A]

    # --- Vth 抽出 ---
    vth_n_low = extract_vth_const_id(vg_n_low, id_n_low, IREF, pmos=False)
    vth_n_high = extract_vth_const_id(vg_n_high, id_n_high, IREF, pmos=False)
    vth_p_low = extract_vth_const_id(vg_p_low, id_p_low, IREF, pmos=True)
    vth_p_high = extract_vth_const_id(vg_p_high, id_p_high, IREF, pmos=True)

    print("\n==== Vth (const-Id, Iref=1.0e-07 A) ====")
    print(f"nMOS Vth_low  (Vd=0.05V)  = {vth_n_low:+.3f} V")
    print(f"nMOS Vth_high (Vd=1.00V) = {vth_n_high:+.3f} V")
    print(f"pMOS Vth_low  (Vd=0.05V)  = {vth_p_low:+.3f} V")
    print(f"pMOS Vth_high (Vd=1.00V) = {vth_p_high:+.3f} V")

    # --- DIBL ---
    dv_n = 1.0 - 0.05
    dv_p = 1.0 - 0.05
    dibl_n = (vth_n_low - vth_n_high) / dv_n * 1e3  # [mV/V]
    dibl_p = (vth_p_low - vth_p_high) / dv_p * 1e3  # [mV/V]

    print("\n==== DIBL (const-Id) ====")
    print(f"nMOS DIBL = {dibl_n:.1f} mV/V")
    print(f"pMOS DIBL = {dibl_p:.1f} mV/V")

    # --- プロット ---
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    # nMOS
    ax = axes[0]
    ax.semilogy(vg_n_low, id_n_low, "b.", label="nMOS Vd=0.05V")
    ax.semilogy(vg_n_high, id_n_high, "r.", label="nMOS Vd=1.00V")
    ax.axvline(vth_n_low, color="b", ls="--",
               label=f"Vth_low={vth_n_low:+.3f}V")
    ax.axvline(vth_n_high, color="r", ls="--",
               label=f"Vth_high={vth_n_high:+.3f}V")
    ax.set_xlabel("Vg [V]")
    ax.set_ylabel("Id [A]")
    ax.set_title("nMOS Id–Vg (const-Id Vth)")
    ax.grid(True, which="both")
    ax.legend()

    # pMOS
    ax = axes[1]
    ax.semilogy(vg_p_low, id_p_low, "b.", label="pMOS Vd=0.05V")
    ax.semilogy(vg_p_high, id_p_high, "r.", label="pMOS Vd=1.00V")
    ax.axvline(vth_p_low, color="b", ls="--",
               label=f"Vth_low={vth_p_low:+.3f}V")
    ax.axvline(vth_p_high, color="r", ls="--",
               label=f"Vth_high={vth_p_high:+.3f}V")
    ax.set_xlabel("Vg [V]")
    ax.set_ylabel("Id [A]")
    ax.set_title("pMOS Id–Vg (const-Id Vth)")
    ax.grid(True, which="both")
    ax.legend()

    plt.tight_layout()
    out_path = FIG_DIR / "dibl.png"
    plt.savefig(out_path, dpi=150)
    print(f"\nSaved figure to: {out_path}")
    # plt.show()


if __name__ == "__main__":
    main()
