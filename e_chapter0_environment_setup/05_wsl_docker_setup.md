# 🛠️ 05_wsl_docker_setup  
**WSL2 ＋ Docker ＋ OpenLane 実行環境セットアップ（中厚版）**  
*WSL2 + Docker + OpenLane Runtime Environment Setup (Mid-Level Version)*

---

## 📘 概要｜Overview
本節では、OpenLane・Magic・Netgen を **Windows 11 上で確実に動作させるための  
WSL2 ＋ Docker 統合環境**を構築します。  
*This section explains how to configure a reliable WSL2 + Docker environment for running OpenLane, Magic, and Netgen on Windows 11.*

---

## ✅ 1. WSL2 を有効化｜*Enable WSL2*

### ❗ まず WSL を有効化  
PowerShell（管理者）で：

```powershell
wsl --install
```

自動的に Ubuntu がインストールされます。  
*This installs WSL2 and Ubuntu automatically.*

### ✅ 状態確認  
```powershell
wsl --status
```

---

## ✅ 2. Ubuntu セットアップ｜*Configure Ubuntu*

Ubuntu 起動後：

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install git make python3-pip -y
```

---

## ✅ 3. Docker Desktop のインストール｜*Install Docker Desktop*

🔗 https://www.docker.com/products/docker-desktop/

### ✅ 必須設定  
- ✅ **WSL2 backend を有効化**  
- ✅ Ubuntu を `integration` で ON  

Docker Desktop → Settings → Resources → WSL Integration

---

## ✅ 4. Docker の動作確認｜*Verify Docker*

```bash
docker --version
docker ps
```

出力されれば OK。

---

## ✅ 5. OpenLane 用ディレクトリ｜*Create Directory Structure*

```
~/openlane/
 ├── pdks/
 └── designs/
```

作成：

```bash
mkdir -p ~/openlane/pdks
mkdir -p ~/openlane/designs
```

---

## ✅ 6. volare で PDK を取得｜*Download Sky130 PDK with volare*

```bash
pip install volare
volare enable sky130A
```

完了後：

```
~/.volare/sky130A/
```

---

## ✅ 7. PDK を OpenLane パスにコピー｜*Copy PDK to OpenLane Path*

```bash
cp -r ~/.volare/sky130A ~/openlane/pdks/
```

---

## ✅ 8. OpenLane コンテナの実行｜*Run OpenLane Container*

### ✅ 最低限の実行例  
```bash
docker run --rm -it   -v "$HOME/openlane/pdks":/pdks   -v "$HOME/openlane/designs":/openlane/designs   -e PDK_ROOT=/pdks   -e PDK=sky130A   efabless/openlane:2024.09.11 bash
```

---

## ✅ 9. WSL2 ＋ Docker ＋ OpenLane の構造図｜*Architecture Diagram*

```mermaid
graph TD
    A[🪟 Windows 11] --> B[🐧 WSL2 Ubuntu]
    B --> C[🐳 Docker Engine]
    C --> D[📦 OpenLane Container]
    D --> E[📁 /pdks (Sky130A)]
    D --> F[📁 /openlane/designs]

    style A fill:#e3f2fd,stroke:#1565c0
    style B fill:#e8f5e9,stroke:#2e7d32
    style C fill:#fff3e0,stroke:#ef6c00
    style D fill:#ede7f6,stroke:#4527a0
    style E fill:#f1f8e9,stroke:#7cb342
    style F fill:#e1f5fe,stroke:#0288d1
```

---

## ✅ 10. よくあるトラブルと対処｜*Common Issues & Fixes*

| 問題 / Issue | 原因 / Cause | 対応 / Fix |
|--------------|--------------|------------|
| Docker が動かない | WSL integration OFF | Docker → Settings → WSL Integration |
| OpenLane で PDK not found | パス未指定 | `-e PDK_ROOT=/pdks` |
| extract で「Cannot open output file」 | 権限不足 | `sudo chown -R $USER:$USER RUN_DIR` |

---

## ✅ 11. チェックリスト｜*Setup Checklist*

| 項目 | OK? |
|------|-----|
| WSL2 有効 | ✅ |
| Ubuntu セットアップ完了 | ✅ |
| Docker Desktop 動作 | ✅ |
| volare で PDK 取得 | ✅ |
| OpenLane コンテナ起動 | ✅ |

---

## 👤 Author
三溝 真一（Shinichi Samizo）  
GitHub: https://github.com/Samizo-AITL
