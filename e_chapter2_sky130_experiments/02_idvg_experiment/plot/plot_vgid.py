# plot_vgid.py - SPICEログから Vg–Id 特性を描画・保存

import matplotlib.pyplot as plt
import os

def parse_log(filepath):
    vg_list = []
    id_list = []

    with open(filepath, 'r') as f:
        for line in f:
            if line.strip().startswith("Index") or line.strip() == "":
                continue
            tokens = line.strip().split()
            if len(tokens) >= 3:
                try:
                    vg = float(tokens[2])
                    id_val = float(tokens[1]) * -1e6  # μAに変換（符号反転）
                    vg_list.append(vg)
                    id_list.append(id_val)
                except ValueError:
                    continue
    return vg_list, id_list

# --- ファイルパス
nfet_log = "output/nfet_vgid.log"
pfet_log = "output/pfet_vgid.log"

# --- ログ存在チェック
if not os.path.exists(nfet_log) or not os.path.exists(pfet_log):
    print("エラー：必要な .log ファイルが存在しません。先に run_check.sh を実行してください。")
    exit(1)

# --- データ読み込み
vg_n, id_n = parse_log(nfet_log)
vg_p, id_p = parse_log(pfet_log)

# --- プロット
plt.figure(figsize=(8, 5))
plt.plot(vg_n, id_n, label='nMOS (nfet_01v8)', marker='o')
plt.plot(vg_p, id_p, label='pMOS (pfet_01v8)', marker='x')
plt.axhline(0, color='gray', linestyle='--', linewidth=0.5)
plt.xlabel('Gate Voltage Vg [V]')
plt.ylabel('Drain Current Id [μA]')
plt.title('Vg–Id Characteristics of Sky130 MOSFETs')
plt.grid(True)
plt.legend()
plt.tight_layout()

# --- PNGファイルとして保存
plt.savefig("output/vgid_plot.png")
print("✅ プロット完了：output/vgid_plot.png に保存されました。")

# --- 画面にも表示
plt.show()
