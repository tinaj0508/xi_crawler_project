import requests
from google.cloud import tasks_v2
from random import randint
from time import sleep
import json

# 初始化 Cloud Tasks 客戶端
client = tasks_v2.CloudTasksClient()

# 配置 Cloud Tasks
project = "master-experiment"
location = "us-central1"
queue = "crawler-tasks2"
url = "https://process-task-service-196413881373.us-central1.run.app"  # Cloud Run 處理爬蟲任務的端點

parent = client.queue_path(project, location, queue)

def create_task(payload):
    """創建 Cloud Tasks 任務"""
    task = {
        "http_request": {
            "http_method": tasks_v2.HttpMethod.POST,
            "url": url,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(payload).encode(),
        }
    }
    response = client.create_task(parent=parent, task=task)
    print(f"Created task {response.name}")

def handle_crawler_tasks(request):
    """發送爬蟲任務到 Cloud Tasks"""
    session_requests = requests.session()
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
    }

    # 爬取的頁面範圍
    for i in range(0,3):  # 調整頁碼範圍
        page_url = f"http://jhsjk.people.cn/testnew/result?keywords=%E4%B9%A0%E8%BF%91%E5%B9%B3&isFuzzy=0&searchArea=0&year=0&form=0&type=0&page={i}&origin=%E5%85%A8%E9%83%A8&source=2"
        sleep(randint(1, 3))  # 避免被封禁
        response = session_requests.get(page_url, headers=header)

        if response.status_code == 200:
            data = response.json()
            for item in data.get("list", []):
                task_payload = {
                    "title": item["title"],
                    "pubtime": item["input_date"],
                    "url": f"http://jhsjk.people.cn/article/{item['article_id']}",
                    "source": item["origin_name"]
                }
                # 發佈到 Cloud Tasks
                create_task(task_payload)

    return "Tasks created", 200