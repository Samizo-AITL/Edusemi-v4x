# plot_vgid.py
# SPICE出力ログからVg–Id特性を描画するPythonスクリプト

import sys
import matplotlib.pyplot as plt

def parse_log(filepath):
    vg = []
    id = []
    with open(filepath, 'r') as f:
        for line in f:
            if line.strip().startswith("v(g)") or line.strip().startswith("V(G)"):
                continue  # skip header
            try:
                parts = line.strip().split()
                if len(parts) >= 2:
                    vg.append(float(parts[0]))
                    id.append(float(parts[1]))
            except:
                continue
    return vg, id

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 plot_vgid.py <logfile1> [<logfile2> ...]")
        sys.exit(1)

    for filepath in sys.argv[1:]:
        vg, id = parse_log(filepath)
        label = filepath.split('/')[-1].replace('.log', '')
        plt.plot(vg, id, label=label)

    plt.xlabel("Gate Voltage Vg [V]")
    plt.ylabel("Drain Current Id [A]")
    plt.title("Vg–Id Characteristics (from SPICE log)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
