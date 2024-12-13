import os
import requests
from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
from google.cloud import storage

app = Flask(__name__)

# 初始化 Cloud Storage 客戶端
storage_client = storage.Client()
BUCKET_NAME = "xi_test_bucket"  # 直接指定存儲桶名稱

@app.route('/process-task', methods=['POST'])
def process_task():
    """處理爬蟲任務並存儲結果到 Cloud Storage"""
    task_data = request.get_json()
    article_url = task_data["url"]

    try:
        # 爬取文章內容
        response = requests.get(article_url, timeout=30)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        content_div = soup.find("div", class_="d2txt_con clearfix")

        if content_div:
            content = content_div.get_text(strip=True)

            # 將結果存儲到 Cloud Storage
            bucket = storage_client.bucket(BUCKET_NAME)
            blob = bucket.blob(f"{task_data['title']}.txt")
            blob.upload_from_string(content, content_type="text/plain")

            print(f"Saved {task_data['title']} to Cloud Storage.")
            return jsonify({"status": "success", "title": task_data["title"]}), 200
        else:
            return jsonify({"status": "failed", "reason": "Content not found"}), 404

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)