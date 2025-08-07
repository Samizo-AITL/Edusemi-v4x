import os
from pathlib import Path

output_md = Path("report_output/auto_report.md")
image_dir = Path("images")
csv_dir = Path("results")

output_md.parent.mkdir(parents=True, exist_ok=True)

with open(output_md, "w") as f:
    f.write("# 自動レポート生成\n\n")

    # PNG挿入
    for png in sorted(image_dir.glob("*.png")):
        f.write(f"## 図：{png.stem}\n")
        f.write(f"![{png.stem}](../images/{png.name})\n\n")

    # CSV挿入（表形式）
    for csv in sorted(csv_dir.glob("*.csv")):
        f.write(f"## 表：{csv.stem}\n")
        df = pd.read_csv(csv)
        f.write(df.to_markdown(index=False))
        f.write("\n\n")

print("✅ Markdown report generated.")
