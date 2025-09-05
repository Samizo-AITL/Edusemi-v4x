* ============================================================
* Toy models mimicking FinFET/GAA tendencies (Level=1 for education)
* Replace with BSIM-CMG etc. for rigorous analysis.
* ============================================================

* FinFET-ish
.model NFIN NMOS(level=1 VTO=0.40 KP=350e-6 LAMBDA=0.04)
.model PFIN PMOS(level=1 VTO=-0.45 KP=150e-6 LAMBDA=0.04)

* GAA-ish (slightly higher gm, lower Vth)
.model NGAA NMOS(level=1 VTO=0.35 KP=420e-6 LAMBDA=0.05)
.model PGAA PMOS(level=1 VTO=-0.38 KP=180e-6 LAMBDA=0.05)
