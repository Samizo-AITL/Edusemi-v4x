# model_constants.py

# 物理定数
BOLTZMANN_CONST = 8.617e-5  # ボルツマン定数 [eV/K]

# BTIモデル用定数
BTI_N = 0.2                 # 時間依存係数
BTI_EA = 0.15               # 活性化エネルギー [eV]
BTI_A = 1e-3                # スケーリング定数（ΔVth初期値）

# TDDBモデル用定数
TDDB_N_LIST = [2, 3, 4]     # フィールドパワーモデルの指数
TDDB_GAMMA_LIST = [-2, -3]  # Eモデルの感度係数

# 温度リスト（絶対温度 [K]）
TEMP_LIST = [298, 358, 398]  # 25°C, 85°C, 125°C
TEMP_LABELS = ["25°C", "85°C", "125°C"]
