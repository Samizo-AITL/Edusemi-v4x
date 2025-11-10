#!/usr/bin/env python3
import argparse
import pandas as pd
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser(description="Plot Vg–Id curve from CSV")
    parser.add_argument("csv", help="input CSV (nfet_vgid.csv / pfet_vgid.csv)")
    parser.add_argument("--out", default="vgid.png", help="output PNG")
    args = parser.parse_args()

    # CSV 読み込み
    df = pd.read_csv(args.csv, sep=r"\s+", comment="#", names=["Vg", "Id"])

    # グラフ
    plt.figure(figsize=(6,4))
    plt.plot(df["Vg"], df["Id"])
    plt.xlabel("Gate Voltage Vg (V)")
    plt.ylabel("Drain Current Id (A)")
    plt.grid(True)

    # タイトルは CSV 名から自動生成
    if "nfet" in args.csv.lower():
        plt.title("NFET Vg–Id")
    elif "pfet" in args.csv.lower():
        plt.title("PFET Vg–Id")
    else:
        plt.title("Vg–Id Curve")

    plt.tight_layout()
    plt.savefig(args.out, dpi=300)
    print(f"Saved: {args.out}")

if __name__ == "__main__":
    main()
