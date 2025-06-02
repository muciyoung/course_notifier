# _*_ coding:utf-8 _*_
# @日期:2025/5/30
# @作者: muci
import requests
from datetime import datetime
import json
import re
import pytz
import sys
from config import PUSHPLUS_TOKEN, JSON_FILE_PATH


def extract_time_and_section(jieci_str):
    time_match = re.search(r'(\d{2}:\d{2})-(\d{2}:\d{2})', jieci_str)
    section_match = re.match(r'([\d\-节]+)', jieci_str)
    time = f"{time_match.group(1)} - {time_match.group(2)}" if time_match else ''
    section = section_match.group(1) if section_match else ''
    return time, section


def render_html(course_list):
    if not course_list:
        return "<p style='text-align:center; color:gray;'>今日无课程安排 🎉</p>"

    card_template = '''
<div style="max-width:600px; margin:12px auto; padding:12px 14px; background:#fff; border:1px solid #ddd; border-radius:8px; box-shadow:0 1px 3px rgba(0,0,0,0.05); color:#333;">
  <div style="font-weight:bold; font-size:1rem; color:#34495e;">{课程名}</div>
  <div style="font-size:0.9rem; color:#666; margin-top:4px;">
    📅 {日期}（{星期}）<br>
    ⏰ {时间段}（{节次}）<br>
    🧑‍🏫 {教师} | 🏫 {教室}
  </div>
</div>
'''
    return ''.join([
        card_template.format(
            课程名=course.get("课程名", ""),
            日期=course.get("日期", ""),
            星期=course.get("星期", ""),
            时间段=extract_time_and_section(course.get("节次", ""))[0],
            节次=extract_time_and_section(course.get("节次", ""))[1],
            教师=course.get("教师", ""),
            教室=course.get("教室", "")
        )
        for course in course_list
    ])


def main():
    if not PUSHPLUS_TOKEN:
        print("错误：请设置 PUSHPLUS_TOKEN 环境变量")
        sys.exit(1)

    try:
        with open(JSON_FILE_PATH, "r", encoding="utf-8") as f:
            courses = json.load(f)
    except Exception as e:
        print(f"读取课程文件失败: {e}")
        sys.exit(1)

    # 指定北京时间时区
    beijing_tz = pytz.timezone("Asia/Shanghai")
    # 获取当前北京时间（含时区信息）
    beijing_now = datetime.now(beijing_tz).strftime('%Y-%m-%d')
    today_courses = [c for c in courses if c.get("日期") == beijing_now]
    html_content = render_html(today_courses)
    title = (
        f"今日无课！快乐摸鱼~ 🎉"
        if not today_courses else
        f"📅今日课程提醒"
    )
    payload = {
        "token": PUSHPLUS_TOKEN,
        "topic": "group001",
        "title": title,
        "content": html_content,
        "template": "html"
    }

    try:
        resp = requests.post("http://www.pushplus.plus/send", json=payload, timeout=10)
        print("响应内容:", resp.json())
        if resp.status_code != 200:
            sys.exit(2)
    except Exception as e:
        print(f"推送失败: {e}")
        sys.exit(2)


if __name__ == "__main__":
    main()