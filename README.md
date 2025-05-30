
# 📅 Course Notifier 自动课程推送器

每天早上定时将课程表以 **卡片式 HTML** 样式，通过 [PushPlus](https://pushplus.plus/) 推送到微信，优雅提醒每日课程安排。

> 💡 自动运行，颜值在线，适合学生党用来定时查看课表。

---

## 🚀 功能亮点

- ⏰ 每天 **北京时间早上 8 点自动推送**
- ✅ 支持 [GitHub Actions](https://docs.github.com/en/actions) 自动部署，无需本地运行
- 💬 使用 **PushPlus 推送服务**，可接收消息到微信
- 🎨 推送样式为卡片式 HTML，美观易读
- 📅 今日无课自动提示 🎉

---

## 📦 项目结构

```

course\_notifier/
├── .github/workflows/notify.yml    # GitHub Actions 定时脚本
├── fangzheng.json                  # 课程数据（源 JSON 文件）
├── main.py                         # 主程序逻辑
├── config.py                       # 环境配置（如 PushPlus Token）
├── requirements.txt                # Python 依赖
└── README.md                       # 项目说明文档

````

---

## 📸 示例推送效果

> HTML 卡片样式，清晰展示课程信息

![](https://cdn.jsdelivr.net/gh/muciyoung/picgo_blog/uPic/814112E9BF34015CA3E7BAA38959BD77.jpg)

![](https://cdn.jsdelivr.net/gh/muciyoung/picgo_blog/uPic/CA47A6F4FDEA783557EFCED8C3779719.jpg)

![](https://cdn.jsdelivr.net/gh/muciyoung/picgo_blog/uPic/WeChat05f3fe74c6b0809f26ec9401c325e84e.jpg)

---

## 🛠️ 快速使用指南

1. **克隆仓库：**

```bash
   git clone https://github.com/muciyoung/course_notifier.git
   cd course_notifier
````

2. **准备课程数据文件：**

   将你的课程表数据保存为 `fangzheng.json`，格式参见示例。

3. **配置 GitHub Secrets：**

   在你的仓库中设置：

   * `PUSHPLUS_TOKEN`：你的 PushPlus 推送 token

4. **GitHub Actions 定时运行：**

   自动每天早上 8:00（北京时间）运行，无需手动干预。

---

## 📄 课程数据格式示例（fangzheng.json）

```json
[
  {
    "课程名": "数据结构",
    "教师": "李老师",
    "节次": "01-02节 08:00-09:50",
    "日期": "2025-05-30",
    "星期": "星期五",
    "教室": "教学楼A201"
  }
]
```

