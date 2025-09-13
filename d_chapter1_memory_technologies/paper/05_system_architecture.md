# 5. システムアーキテクチャ
- コア電源：1.8 V（ロジック、SRAM、FeFETを統一）  
- FeFET書込み：内部チャージポンプで ±2.5 V パルスを生成、1–50 µs幅  
- SRAM ⇄ FeFET 間に専用転送回路を設け、電断時に即バックアップ、復帰時にリストア  
- 外周3.3 Vは I/O および AMS 用にオプション追加可能  

**図6-1**: 電源ドメイン構成  

```mermaid
flowchart TB
    subgraph Core["Core 1.8V"]
        L[Logic]
        S[SRAM]
        F[FeFET NVM]
        P[Charge Pump\n±2.5V]
    end

    subgraph Periphery["3.3V I/O & AMS (Option)"]
        IO[I/O PAD]
        AMS[ADC/DAC, LDO]
    end

    %% connections
    L --> S
    S <--> F
    P --> F

    Core --> Periphery
```

**図6-2**: バックアップ／リストア経路

```mermaid
flowchart TB
    S[SRAM] -->|電断検知→バックアップ| C[バックアップコントローラ]
    C --> F[FeFET NVM]

    F -->|復帰時ロード| C2[復帰制御]
    C2 --> S
```

