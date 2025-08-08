# summary_bti_tddb.py: BTIとTDDBの結果を統合表示

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

data_dir = "data"
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# BTIデータ読み込みとプロット
bti_file = os.path.join(data_dir, "bti_data.csv")
if os.path.exists(bti_file):
    bti_df = pd.read_csv(bti_file)
    plt.figure()
    for temp in bti_df["Temp[K]"].unique():
        sub = bti_df[bti_df["Temp[K]"] == temp]
        plt.plot(sub["Time[s]"], sub["DeltaVth[V]"], label=f"{int(temp)} K")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Time [s]")
    plt.ylabel("ΔVth [V]")
    plt.title("BTI Degradation vs Time")
    plt.grid(True)
    plt.legend()
    plt.savefig(os.path.join(output_dir, "bti_degradation.png"))
    plt.close()
else:
    print("No BTI data found.")

# TDDBデータ読み込みとプロット
tddb_file = os.path.join(data_dir, "tddb_data.csv")
if os.path.exists(tddb_file):
    tddb_df = pd.read_csv(tddb_file)
    plt.figure()
    for model in tddb_df["Model"].unique():
        sub = tddb_df[tddb_df["Model"] == model]
        plt.plot(sub["E_field"], sub["MTTF"], label=model)
    plt.xlabel("Electric Field [MV/cm]")
    plt.ylabel("MTTF [s]")
    plt.yscale("log")
    plt.title("TDDB Models - MTTF vs Electric Field")
    plt.grid(True)
    plt.legend()
    plt.savefig(os.path.join(output_dir, "tddb_models.png"))
    plt.close()
else:
    print("No TDDB data found.")
