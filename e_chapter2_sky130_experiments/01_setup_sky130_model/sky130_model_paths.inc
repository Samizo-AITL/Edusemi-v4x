* sky130_model_paths.inc - Sky130 SPICE model include for ngspice

* モデルファイルの場所（PDK インストールパスに合わせて修正）
.include "~/pdks/sky130A/libs.tech/ngspice/sky130.lib.spice"

* コーナー指定：typical-typical を使用
.lib "~/pdks/sky130A/libs.tech/ngspice/sky130.lib.spice" tt
