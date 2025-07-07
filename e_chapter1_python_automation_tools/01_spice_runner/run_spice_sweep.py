import os
import json
import subprocess
from pathlib import Path

def generate_spice_file(template_path, w, l, vds, out_path):
    with open(template_path, "r") as f:
        spice = f.read()
    spice = spice.replace("{{W}}", str(w))
    spice = spice.replace("{{L}}", str(l))
    spice = spice.replace("{{VDS}}", str(vds))
    with open(out_path, "w") as f:
        f.write(spice)

def run_ngspice(spice_file, output_log):
    result = subprocess.run(
        ["ngspice", "-b", "-o", output_log, spice_file],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    print(result.stdout)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")

def main():
    with open("config.json") as f:
        cfg = json.load(f)

    out_dir = Path(cfg["output_dir"])
    out_dir.mkdir(exist_ok=True)

    prefix = cfg.get("output_csv_prefix", "vgid")

    for w in cfg["w"]:
        for l in cfg["l"]:
            fname = f"{prefix}_W{w}_L{l}.spice"
            fpath = out_dir / fname
            generate_spice_file(cfg["spice_template"], w, l, cfg["vd"], fpath)

            logname = f"{prefix}_W{w}_L{l}.log"
            logpath = out_dir / logname
            run_ngspice(str(fpath), str(logpath))

if __name__ == "__main__":
    main()
