# plot_vgid.py - SPICEログから Vg-Id 特性を描画

import matplotlib.pyplot as plt

def parse_log(filename):
    vg_list = []
    id_list = []

    with open(filename, 'r') as f:
        for line in f:
            if line.strip().startswith("Index"):
                continue
            tokens = line.strip().split()
            if len(tokens) >= 4:
                try:
                    vg = float(tokens[2])
                    id_val = float(tokens[1]) * -1e6  # µA に変換（符号反転）
                    vg_list.append(vg)
                    id_list.append(id_val)
                except ValueError:
                    continue
    return vg_list, id_list

# --- ファイル指定（必要に応じて変更）
nfet_log = "output/nfet_vgid.log"
pfet_log = "output/pfet_vgid.log"

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
plt.show()
