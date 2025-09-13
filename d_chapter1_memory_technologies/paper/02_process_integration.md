# 2. プロセス統合
- ベースライン：0.18 µm CMOS (1.8 V ロジック、3.3 V SRAM/I/O)  
- FeFETモジュールは Poly 定義後、Coシリサイド形成とランプアニール後に挿入  
- スタック構成：TiN / HZO (8–12 nm, ALD) / Al₂O₃ (1–2 nm, ALD) / p-Si  
- **図1**: プロセス断面およびフロー図

```mermaid
flowchart TD
    A["① FEOL完了<br/>(Coシリサイド／ランプアニール)"] --> B["② ダミーポリ除去<br/>(SiON/SiN ハードマスク)"]
    B --> C["③ ALD: Al₂O₃ (1–2 nm)"]
    C --> D["④ ALD: HZO (8–12 nm)"]
    D --> E["⑤ スパッタ: TiN (30–50 nm)"]
    E --> F["⑥ RTA (450–500℃)"]
    F --> G["⑦ BEOL配線"]
```

```mermaid
flowchart BT
    PSi["p-Si 基板"] --> IL["Al₂O₃ 1–2 nm (ALD)"]
    IL --> HZO["HZO 8–12 nm (ALD)"]
    HZO --> TiN["TiN 30–50 nm (SP)"]
```
