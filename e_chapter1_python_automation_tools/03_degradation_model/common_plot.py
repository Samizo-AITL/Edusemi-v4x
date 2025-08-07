# common_plot.py

import matplotlib.pyplot as plt

def setup_plot(title, xlabel, ylabel):
    plt.figure(figsize=(6, 4))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)

def finalize_plot(save_path):
    plt.tight_layout()
    plt.savefig(save_path)
    print(f"Saved plot to: {save_path}")
    plt.show()
