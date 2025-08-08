# summary_vth.py: Vth抽出結果をまとめて可視化

import pandas as pd
import matplotlib.pyplot as plt
import os

# データフォルダと出力フォルダ
data_dir = "data"
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# CSVファイルの読み込み
vth_data = []
for file in os.listdir(data_dir):
    if file.endswith(".csv") and "vth" in file:
        df = pd.read_csv(os.path.join(data_dir, file))
        vth_data.append(df)

# データの統合
if vth_data:
    all_vth = pd.concat(vth_data)
    all_vth = all_vth.sort_values(by=["W", "L"])

    # プロット（W/L vs Vth）
    all_vth["W/L"] = all_vth["W"] / all_vth["L"]
    plt.figure(figsize=(8, 6))
    for device in all_vth["device"].unique():
        subset = all_vth[all_vth["device"] == device]
        plt.plot(subset["W/L"], subset["Vth"], marker="o", label=device)

    plt.xlabel("W/L Ratio")
    plt.ylabel("Threshold Voltage Vth [V]")
    plt.title("Vth vs W/L Ratio")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "vth_vs_wl.png"))
    plt.close()
else:
    print("No Vth CSV data found.")
