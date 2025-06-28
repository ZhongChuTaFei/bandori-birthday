import json
import logging
from datetime import datetime
import pytz
import os
import requests

# 设置日志格式（东京时间）
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s][%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logging.Formatter.converter = lambda *args: datetime.now(pytz.timezone("Asia/Tokyo")).timetuple()

WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # 从环境变量读取 webhook

def load_birthdays(file_path='birthdays.json'):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_today_in_tokyo():
    tz_tokyo = pytz.timezone('Asia/Tokyo')
    dt = datetime.now(tz_tokyo)
    return dt.strftime("%m-%d"), f"{int(dt.month)}月{int(dt.day)}日"

def build_message(entry, readable_date):
    if len(entry) == 4:
        role, band, position, date = entry
        return f"现在是日本时间{readable_date}，{band}的{position}，**{role}**的生日，祝她生日快乐🎉！", role
    elif len(entry) == 5:
        name, role, band, position, date = entry
        return f"现在是日本时间{readable_date}，{band}的{position}，{role}的声优**{name}**的生日，祝她生日快乐🎉！", name
    return None, None

def send_message(msg):
    body = {
        "msgtype": "markdown",
        "markdown": {
            "content": f"# 邦多利生日提醒\n{msg}"
        }
    }
    response = requests.post(WEBHOOK_URL, json=body)
    logging.info(f"已发送生日祝贺，内容: {msg}，状态码: {response.status_code}")

def main():
    birthdays = load_birthdays()
    date_raw, readable_date = get_today_in_tokyo()

    for entry in birthdays:
        date = entry[-1]
        if date == date_raw:
            msg, identifier = build_message(entry, readable_date)
            if msg:
                send_message(msg)
                logging.info(f"已发送 {identifier} 的生日祝贺")

if __name__ == "__main__":
    main()
