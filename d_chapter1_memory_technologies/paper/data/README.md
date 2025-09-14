# FeFET Reliability CSV Pack (v2)

This pack contains reproducible CSV templates for reliability analysis of a 0.18 µm FeFET/FeCAP stack (TiN/HZO/Al2O3). 
Random seed fixed at 42 for repeatability.

## Files
- tzdb_results.csv — TZDB breakdown distribution (flat & comb patterns), with wafer map and zone.
- tddb_results.csv — TDDB lifetimes at 3 stress voltages (2.3/2.5/2.7 V) × 2 temps (85/125 °C), 30 devices/condition.
- endurance_results.csv — ΔVth vs cycles for 10 cells at RT/85 °C.
- retention_results.csv — window_norm vs time for 10 cells at 25/85/125 °C (Arrhenius Ea≈1.1 eV).

## Columns (high level)
- Common: lot, wafer, die_x, die_y, zone (CENTER/MIDDLE/EDGE), tox_nm, Eox_MVcm
- TZDB: pattern (FLAT/COMB), temp_C, area_cm2, Vbd_V
- TDDB: temp_C, stress_V, beta_shape(=1.3), eta_scale_est_ref, time_to_failure_s
- Endurance: temp_C, cycles, delta_Vth_V
- Retention: temp_C, time_s, window_norm (normalized ΔVth window), tau50_ref_85C_s, Ea_eV

## Notes
- Eox = V / tox; tox=10 nm assumed.
- TZDB totals per temp: FLAT 150 pcs (6.0 cm²) + COMB 80 pcs.
- TDDB uses Weibull with β≈1.3; η scales with voltage and temperature (heuristic for template use).
