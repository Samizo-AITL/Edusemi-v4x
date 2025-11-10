* sky130_model_paths.inc
* Sky130 ngspice model include for NFET/PFET 01v8 devices
* 環境変数:
*   export PDK_ROOT=/mnt/c/openlane/pdks
*   export PDK=sky130A

.lib "$::env(PDK_ROOT)/$::env(PDK)/libs.tech/ngspice/sky130.lib.spice" tt
