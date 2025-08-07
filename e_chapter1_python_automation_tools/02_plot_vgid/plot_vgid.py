#!/usr/bin/env python3
# plot_vgid.py

import sys
import os
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

def parse_and_plot(log_files):
    Path("figures").mkdir(exist_ok=True)

    for log_path in log_files:
        try:
            df = pd.read_csv(log_path, delim_whitespace=True, comment='*')
            if 'V(G)' not in df.columns or 'I(VD)' not in df.columns:
                print(f"Skipping {log_path}: missing expected columns.")
                continue

            plt.plot(df['V(G)'], df['I(VD)'], label=os.path.basename(log_path).replace(".log", ""))
        except Exception as e:
            print(f"Error processing {log_path}: {e}")

    plt.xlabel("Vg [V]")
    plt.ylabel("Id [A]")
    plt.title("Vg–Id Characteristics")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    # 保存
    png_path = "figures/VgId_summary.png"
    pdf_path = "figures/VgId_summary.pdf"
    plt.savefig(png_path)
    plt.savefig(pdf_path)
    print(f"Saved plots to: {png_path}, {pdf_path}")

    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 plot_vgid.py output/*.log")
        sys.exit(1)

    log_files = sys.argv[1:]
    parse_and_plot(log_files)
