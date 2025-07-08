# 5.2 MagicによるGDS階層と層構成の可視化

## 🎯 本節の目的

- Magicを用いてGDSファイルを開き、各レイヤーとセル階層を視覚的に確認する  
- Sky130の物理レイヤー構成を可視化し、設計対象のGDS構造を直感的に把握する

---

## 🖥️ 使用ツール：Magic

MagicはSky130PDKと統合されたオープンソースレイアウトエディタです。  
PDK環境がセットされた状態で以下のようにGDSを開くことができます：

```bash
cd runs/soc_top/results/final/gds/
magic -T sky130A.tech soc_top.gds
```

---

## 🔍 Magic上での主な操作

| 操作内容 | コマンド例／GUI |
|----------|----------------|
| 層の表示切り替え | `Option` → `Display Styles` or `Layer Selection` |
| セル階層の展開 | `Expand Cell`（F5キー）またはコマンド `expand` |
| レイヤー情報確認 | `what` コマンド or マウス右クリック |
| GDS層番号の確認 | `tech` ファイル参照 or レイヤー名表示欄 |

---

## 🧱 可視化の観察ポイント

- `nwell`, `poly`, `li1`, `met1〜met4` など層ごとの物理構造  
- セルインスタンス（例：DFF, INV, AND）の配置と階層構造  
- via構造（`via1`, `via2`）による層間接続の具体的な位置関係  
- コンタクト（`licon`, `mcon`, `via`）の出現位置と配線密度

---

## 🧩 観察例

- `poly`と`nimplant`の重なり → ゲート構造  
- `li1`→`met1` → `met2`への接続ビアの連鎖  
- `soc_top`内のFSM/PIDインスタンス → 層が異なる領域を形成

---

## ✅ 本節まとめ

- MagicはSky130PDKと連携してレイアウト層構成を詳細に可視化可能  
- GDSファイルの階層的構造を理解することは、DFM設計の土台となる  
- 次節では DRC ルールに注目し、Magic上での設計ルールチェックを体験する

---

👉 [5.3 DRCルールとその根拠（例：metal spacing）](5_3_drc_check.md)
