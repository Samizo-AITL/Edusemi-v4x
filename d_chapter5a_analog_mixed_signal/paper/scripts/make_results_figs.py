import numpy as np, matplotlib.pyplot as plt, os

outdir = os.path.join("paper","figures","png")
os.makedirs(outdir, exist_ok=True)

# Fig6: L, Q vs freq
f = np.logspace(7,8,200)   # 10–100 MHz
L_air = 40e-9*(1-0.15*np.log10(f/1e7))
L_mag = 100e-9*(1-0.08*np.log10(f/1e7))
Q_air = 5*(1-0.2*np.log10(f/1e7))
Q_mag = 15*(1-0.1*np.log10(f/1e7))

plt.figure(); plt.loglog(f/1e6, L_air*1e9, label="Air-core L")
plt.loglog(f/1e6, L_mag*1e9, label="Mag+PGS L")
plt.xlabel("Frequency [MHz]"); plt.ylabel("Inductance [nH]"); plt.legend(); plt.grid(True, which="both")
plt.savefig(os.path.join(outdir,"fig6_inductor_L.png"), bbox_inches="tight"); plt.close()

plt.figure(); plt.semilogx(f/1e6, Q_air, label="Air-core Q")
plt.semilogx(f/1e6, Q_mag, label="Mag+PGS Q")
plt.xlabel("Frequency [MHz]"); plt.ylabel("Q factor"); plt.legend(); plt.grid(True, which="both")
plt.savefig(os.path.join(outdir,"fig6_inductor_Q.png"), bbox_inches="tight"); plt.close()

# Fig7: Efficiency vs load
I = np.linspace(0.05,0.5,100)  # 50–500 mA
eta_buck = 0.82 - 0.02*(I.max()-I)/I.max()
eta_ldo  = 0.65 - 0.05*I/I.max()
eta_hyb  = 0.80 - 0.015*(I.max()-I)/I.max()

plt.figure(); plt.plot(I*1e3, 100*eta_buck, label="Buck only")
plt.plot(I*1e3, 100*eta_ldo,  label="LDO only")
plt.plot(I*1e3, 100*eta_hyb,  label="Hybrid Buck→LDO")
plt.xlabel("Load current [mA]"); plt.ylabel("Efficiency [%]"); plt.legend(); plt.grid(True)
plt.savefig(os.path.join(outdir,"fig7_efficiency_comparison.png"), bbox_inches="tight"); plt.close()

# Fig8: PSRR & ripple (placeholder)
f2 = np.logspace(3,7,200)  # 1 kHz–10 MHz
psrr = 20 + 40*(1 - np.log10(f2/1e3)/4)  # >60dB@1MHz相当の雰囲気
psrr = np.clip(psrr, 10, 70)

plt.figure(); plt.semilogx(f2/1e3, psrr)
plt.xlabel("Frequency [kHz]"); plt.ylabel("PSRR [dB]"); plt.grid(True, which="both")
plt.savefig(os.path.join(outdir,"fig8_noise_psrr.png"), bbox_inches="tight"); plt.close()

# Fig9: Transient response (0.1->0.5A)
t = np.linspace(0,5e-6,1000)
v = 1.2 + 0.02*np.exp(-((t-1e-6)/0.4e-6)**2) - 0.015*np.exp(-((t-3e-6)/0.5e-6)**2)
plt.figure(); plt.plot(t*1e6, v)
plt.xlabel("Time [µs]"); plt.ylabel("Vout [V]"); plt.grid(True)
plt.savefig(os.path.join(outdir,"fig9_transient_response.png"), bbox_inches="tight"); plt.close()

# Fig10: Reliability (Q vs Temp, dummy)
T = np.array([-40, 25, 85, 125, 150])
Q = 15*np.ones_like(T) - 0.02*(T-25)
plt.figure(); plt.plot(T, Q, marker="o")
plt.xlabel("Temperature [°C]"); plt.ylabel("Q factor"); plt.grid(True)
plt.savefig(os.path.join(outdir,"fig10_reliability.png"), bbox_inches="tight"); plt.close()

print("Saved PNGs to", outdir)
