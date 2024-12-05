# My Crawler Project

## 目標
- 發佈爬蟲任務到 Cloud Tasks。
- 使用 Cloud Run 處理爬蟲內容並存儲到 Cloud Storage。

## 文件結構
- `cloud_functions/`: 包含 Cloud Functions 的程式碼。
- `cloud_run/`: 包含 Cloud Run 的程式碼與配置。
- `config/`: 配置文件。
- `scripts/`: 自動化腳本。

## 部署
1. 部署 Cloud Functions:
   ```bash
   bash scripts/deploy_functions.sh