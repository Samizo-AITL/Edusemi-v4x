---
layout: default
title: 05 WSL2 + Docker Setup
---

---

# 🛠️ 05_wsl_docker_setup  
**WSL2 ＋ Docker ＋ OpenLane 実行環境セットアップ（詳細版）**  
*WSL2 + Docker + OpenLane Runtime Environment Setup (Enhanced Version)*

---

## 📘 概要｜Overview
本節では、OpenLane・Magic・Netgen を **Windows 11 上で確実に動作**させるための  
**WSL2 ＋ Docker 統合開発環境**を構築します。

This section provides a **stable WSL2 + Docker environment**  
required to run OpenLane, Magic, and Netgen on Windows 11.

---

## ✅ 1. WSL2 を有効化｜*Enable WSL2*

PowerShell（管理者）で以下を実行：

```powershell
wsl --install
```

Ubuntu が自動的にインストールされます。

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
sudo apt install git make python3 python3-pip -y
```

---

## ✅ 3. Docker Desktop のインストール｜*Install Docker Desktop*

🔗 https://www.docker.com/products/docker-desktop/

### ✅ 必須設定  
- ✅ **Use the WSL2 backend** を有効化  
- ✅ Ubuntu の integration を ON  

Docker Desktop → Settings → Resources → **WSL Integration**

---

## ✅ 4. Docker の動作確認｜*Verify Docker*

```bash
docker --version
docker ps
```

---

## ✅ 5. OpenLane 用ディレクトリ作成｜*Create Directories*

```
~/openlane/
 ├── pdks/
 └── designs/
```

作成：

```bash
mkdir -p ~/openlane/pdks ~/openlane/designs
```

---

## ✅ 6. volare で Sky130 PDK を取得｜*Download Sky130 PDK with volare*

```bash
pip install volare
volare enable sky130A
```

インストール場所：

```
~/.volare/sky130A/
```

---

## ✅ 7. PDK を OpenLane パスへコピー｜*Copy PDK to OpenLane Path*

```bash
cp -r ~/.volare/sky130A ~/openlane/pdks/
```

---

## ✅ 8. OpenLane コンテナの実行｜*Run OpenLane Container*

```bash
docker run --rm -it \
  -v "$HOME/openlane/pdks":/pdks \
  -v "$HOME/openlane/designs":/openlane/designs \
  -e PDK_ROOT=/pdks \
  -e PDK=sky130A \
  efabless/openlane:2024.09.11 bash
```

---

## ✅ 9. アーキテクチャ図｜*Architecture Diagram*

```mermaid
graph TD
    A[🪟 Windows 11] --> B[🐧 WSL2 Ubuntu]
    B --> C[🐳 Docker Engine]
    C --> D[📦 OpenLane Container]
    D --> E[📁 /pdks (Sky130A PDK)]
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

| 問題 / Issue | 原因 / Cause | 対策 / Fix |
|--------------|---------------|-------------|
| Docker が動かない | WSL integration が OFF | Docker → Settings → WSL Integration |
| PDK not found | PDK_ROOT 未設定 | `-e PDK_ROOT=/pdks` を指定 |
| extract の write error | 権限不足 | `sudo chown -R $USER:$USER RUN_DIR` |
| コンテナ内で Python 不足 | 写像された WSL 側 Python を使用 | `apt install python3` |

---

## ✅ 11. チェックリスト｜*Setup Checklist*

| 項目 / Item | OK? |
|-------------|-----|
| WSL2 有効化 | ✅ |
| Ubuntu セットアップ | ✅ |
| Docker Desktop 動作 | ✅ |
| WSL Integration ON | ✅ |
| volare による PDK 取得 | ✅ |
| OpenLane コンテナ起動成功 | ✅ |

---

## 👤 Author
三溝 真一（Shinichi Samizo）  
GitHub: https://github.com/Samizo-AITL
