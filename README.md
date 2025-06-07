# AutoAliveMailer

**AutoAliveMailer** 是一个自动发送邮件工具，可在每天固定时间向多个指定邮箱发送邮件，保持邮箱活跃。

## 📦 使用方法

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 设置邮箱账户（创建 `.env` 文件）

```
EMAIL_USER=youremail@gmail.com
EMAIL_PASS=your_app_password
```

### 3. 配置邮件内容（修改 `config.json`）

```json
{
  "receivers": ["user1@example.com", "user2@example.com"],
  "subject": "Keep-alive Email",
  "content": "Hi, this is a regular keep-alive email.",
  "send_time": "09:00"
}
```

### 4. 运行脚本（每天固定时间发送）

```bash
python mailer.py
```

---

📌 默认使用 Gmail SMTP（smtp.gmail.com:465），可修改为其他服务。
