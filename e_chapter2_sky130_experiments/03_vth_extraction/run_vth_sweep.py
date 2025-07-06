import os
import subprocess
import pandas as pd

# 設定パラメータ（複数条件をリスト化）
wl_conditions = [
    {'W': 1.0, 'L': 0.15},
    {'W': 2.0, 'L': 0.3},
    # 必要に応じて追加
]

# テンプレート読み込み
with open("templates/meas_template.spice", "r") as f:
    template = f.read()

# 出力ディレクトリ
os.makedirs("output", exist_ok=True)
results = []

# 各条件でシミュレーション実行
for cond in wl_conditions:
    W, L = cond["W"], cond["L"]
    fname = f"vgid_W{W}_L{L}"
    spice_fname = f"output/{fname}.spice"
    log_fname = f"output/{fname}.log"

    # テンプレート展開
    netlist = template.replace("{{W}}", str(W)).replace("{{L}}", str(L))
    with open(spice_fname, "w") as f:
        f.write(netlist)

    # ngspice 実行
    with open(log_fname, "w") as log:
        subprocess.run(["ngspice", "-b", "-o", log.name, spice_fname], check=True)

    # Vth 抽出（ログから .meas の値を探す）
    with open(log_fname, "r") as f:
        for line in f:
            if "vth =" in line.lower():
                vth_val = float(line.strip().split()[-1])
                results.append({"W": W, "L": L, "Vth": vth_val})

# CSV保存
df = pd.DataFrame(results)
df.to_csv("output/vth_results.csv", index=False)
print(df)
