from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# ルートとディレクトリ設定
ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw"
FIG_DIR = ROOT / "figs"
FIG_DIR.mkdir(exist_ok=True)


def load_vg_id(path: Path):
    """Vg–Id ログを読み込み、Vg 昇順・|Id| で返す"""
    data = np.loadtxt(path)
    vg = data[:, 0]
    id_abs = np.abs(data[:, -1])
    idx = np.argsort(vg)
    return vg[idx], id_abs[idx]


def fit_ss_auto(vg, id_abs, window=15, min_decade_span=1.0):
    """
    サブスレッショルド係数 SS を自動抽出する関数。

    - log10(Id)–Vg をスキャン
    - window 個ずつスライドして直線フィット
    - その区間の log10(Id) の変化が min_decade_span [dec] 以上のものだけを候補に
    - 残差が最小の区間を SS 抽出区間とする
    """
    log_id = np.log10(id_abs)
    n = len(vg)
    if n < window:
        raise RuntimeError("データ点が少なすぎます。window を小さくしてください。")

    best_err = np.inf
    best_a = best_b = None
    best_vg = best_y = None

    for i in range(n - window + 1):
        x = vg[i:i + window]
        y = log_id[i:i + window]

        # ほぼ水平なリーク領域はスキップ（logId が 1 decade 以上変化していない）
        if y.max() - y.min() < min_decade_span:
            continue

        a, b = np.polyfit(x, y, 1)
        y_fit = a * x + b
        err = np.mean((y - y_fit) ** 2)

        if err < best_err:
            best_err = err
            best_a, best_b = a, b
            best_vg, best_y = x, y

    if best_a is None:
        raise RuntimeError(
            "SS 用に十分な変化を持つ領域が見つかりませんでした。"
            "min_decade_span を小さくするか、データレンジを確認してください。"
        )

    # SS [mV/dec] = (ln10 / |slope|) * 1e3
    ss = np.log(10) / abs(best_a) * 1e3
    return ss, (best_a, best_b), best_vg, best_y


def main():
    n_log = RAW_DIR / "vgid_nmos.log"
    p_log = RAW_DIR / "vgid_pmos.log"

    print(f"Loading logs from: {RAW_DIR}")
    vg_n, id_n = load_vg_id(n_log)
    vg_p, id_p = load_vg_id(p_log)

    # SS 自動フィット
    ss_n, (a_n, b_n), vg_n_fit, y_n = fit_ss_auto(vg_n, id_n,
                                                  window=15,
                                                  min_decade_span=1.0)
    ss_p, (a_p, b_p), vg_p_fit, y_p = fit_ss_auto(vg_p, id_p,
                                                  window=15,
                                                  min_decade_span=1.0)

    print(f"nMOS SS = {ss_n:.1f} mV/dec")
    print(f"pMOS SS = {ss_p:.1f} mV/dec")

    # プロット
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    # --- 左: 全体 + フィット区間 ---
    ax = axes[0]
    ax.semilogy(vg_n, id_n, ".", alpha=0.4, label="nMOS")
    ax.semilogy(vg_p, id_p, ".", alpha=0.4, label="pMOS")

    ax.semilogy(vg_n_fit, 10 ** (a_n * vg_n_fit + b_n), "g.",
                label="nMOS fit region")
    ax.semilogy(vg_p_fit, 10 ** (a_p * vg_p_fit + b_p), "r.",
                label="pMOS fit region")

    ax.set_xlabel("Vg [V]")
    ax.set_ylabel("Id [A]")
    ax.set_title("log10(Id)–Vg & selected region")
    ax.grid(True, which="both")
    ax.legend()

    # --- 右: ベスト線形区間の直線表示 ---
    ax = axes[1]
    ax.semilogy(vg_n, id_n, ".", alpha=0.3)
    ax.semilogy(vg_p, id_p, ".", alpha=0.3)

    vg_n_line = np.linspace(vg_n_fit.min(), vg_n_fit.max(), 100)
    vg_p_line = np.linspace(vg_p_fit.min(), vg_p_fit.max(), 100)

    ax.semilogy(
        vg_n_line, 10 ** (a_n * vg_n_line + b_n),
        "g-", label=f"nMOS fit (SS={ss_n:.1f} mV/dec)"
    )
    ax.semilogy(
        vg_p_line, 10 ** (a_p * vg_p_line + b_p),
        "r-", label=f"pMOS fit (SS={ss_p:.1f} mV/dec)"
    )

    ax.set_xlabel("Vg [V]")
    ax.set_ylabel("Id [A]")
    ax.set_title("Best linear region (auto selected)")
    ax.grid(True, which="both")
    ax.legend()

    plt.tight_layout()
    out_path = FIG_DIR / "ss.png"
    plt.savefig(out_path, dpi=150)
    print(f"Saved figure to: {out_path}")
    # plt.show()


if __name__ == "__main__":
    main()
