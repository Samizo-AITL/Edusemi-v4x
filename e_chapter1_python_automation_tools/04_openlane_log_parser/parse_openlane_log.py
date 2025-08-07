import pandas as pd
import matplotlib.pyplot as plt
import json
from pathlib import Path

# 設定ファイルの読み込み
with open("example_config.json", "r") as f:
    config = json.load(f)

log_dir = Path(config["log_dir"])
output_dir = Path(config["output_dir"])
output_dir.mkdir(exist_ok=True)

# metrics.csv の読み込み
metrics_file = log_dir / "metrics.csv"
df = pd.read_csv(metrics_file)

# 出力CSV
summary_csv = output_dir / "summary_table.csv"
df.to_csv(summary_csv, index=False)
print(f"✅ Summary saved to {summary_csv}")

# グラフ描画（例：delay, area, power）
for key in ["delay", "area", "power"]:
    if key in df.columns:
        plt.figure()
        df.plot(x="run_id", y=key, kind="bar", legend=False)
        plt.title(f"{key.capitalize()} Comparison")
        plt.ylabel(key)
        plt.xlabel("Run ID")
        plt.tight_layout()
        fig_path = output_dir / f"{key}_comparison.png"
        plt.savefig(fig_path)
        print(f"📊 Graph saved: {fig_path}")
        plt.close()
