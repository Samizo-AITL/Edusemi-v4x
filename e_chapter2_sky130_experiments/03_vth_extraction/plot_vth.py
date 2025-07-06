import pandas as pd
import matplotlib.pyplot as plt

# CSV読み込み（デフォルトパス）
df = pd.read_csv("output/vth_results.csv")

# グラフ描画（W/Lをラベルとして表示）
plt.figure(figsize=(8, 5))
for wl in df[["W", "L"]].drop_duplicates().values:
    W, L = wl
    vth = df[(df["W"] == W) & (df["L"] == L)]["Vth"].values
    label = f"W={W}µm, L={L}µm"
    plt.plot([L], vth, 'o', label=label)

plt.xlabel("チャネル長 L (µm)")
plt.ylabel("しきい値電圧 Vth (V)")
plt.title("W/L条件ごとのVth特性")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("output/vth_plot.png")
plt.show()
