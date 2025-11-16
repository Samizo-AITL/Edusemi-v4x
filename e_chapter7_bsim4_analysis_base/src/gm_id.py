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
    idx = np.argsort(vg)
    return vg[idx], id_abs[idx]


def main():
    n_log = RAW_DIR / "vgid_nmos.log"
    p_log = RAW_DIR / "vgid_pmos.log"

    print(f"NMOS_LOG = {n_log}")
    print(f"PMOS_LOG = {p_log}")

    vg_n, id_n = load_vg_id(n_log)
    vg_p, id_p = load_vg_id(p_log)

    # gm = dId/dVg
    gm_n = np.gradient(id_n, vg_n)
    gm_p = np.gradient(id_p, vg_p)

    # gm/Id
    gm_id_n = gm_n / id_n
    gm_id_p = gm_p / id_p

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    # gm–Vg
    ax = axes[0]
    ax.plot(vg_n, gm_n, label="nMOS")
    ax.plot(vg_p, gm_p, label="pMOS")
    ax.set_xlabel("Vg [V]")
    ax.set_ylabel("gm [S]")
    ax.set_title("gm–Vg")
    ax.grid(True)
    ax.legend()

    # gm/Id–Vg
    ax = axes[1]
    ax.plot(vg_n, gm_id_n, label="nMOS")
    ax.plot(vg_p, gm_id_p, label="pMOS")
    ax.set_xlabel("Vg [V]")
    ax.set_ylabel("gm/Id [V^-1]")
    ax.set_title("gm/Id–Vg")
    ax.grid(True)
    ax.legend()

    plt.tight_layout()
    out_path = FIG_DIR / "gm_id.png"
    plt.savefig(out_path, dpi=150)
    print(f"Saved figure to: {out_path}")
    # plt.show()


if __name__ == "__main__":
    main()
