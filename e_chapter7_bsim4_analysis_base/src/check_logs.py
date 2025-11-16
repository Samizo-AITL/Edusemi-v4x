import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).parent

for name in ["vgid_nmos.log", "vgid_pmos.log"]:
    path = BASE_DIR / name
    data = np.loadtxt(path)
    print("===" , name, "===")
    print("shape:", data.shape)
    print("first row :", data[0, :])
    print("last  row :", data[-1, :])
