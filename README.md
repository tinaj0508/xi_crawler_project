# 用習近平來測試

## 目標
- **Cloud function** 抓取習近平重要講話資料庫標題時間連結。
- 將文章列表中的每篇文章處理為單獨的任務，透過 **Cloud Tasks** 將任務派發至 **Cloud Run** 進行處理。
- **Cloud Run** 負責爬取文章內文並存儲到 **Cloud Storage**。(未成功)

## 文件結構
- `cloud_functions/`: 包含 Cloud Functions 的程式碼。
- `cloud_run/`: 包含 Cloud Run 的程式碼與配置。
- `config/`: 配置文件。
- `scripts/`: 自動化腳本。
