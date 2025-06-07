import smtplib
import json
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import schedule
import time
from datetime import datetime

load_dotenv()

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def send_email(config):
    sender = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")
    receivers = config["receivers"]

    subject = config["subject"]
    content = config["content"]

    msg = MIMEMultipart()
    msg["From"] = sender
    msg["Subject"] = subject
    msg.attach(MIMEText(content, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            for receiver in receivers:
                msg["To"] = receiver
                server.sendmail(sender, receiver, msg.as_string())
                print(f"[{datetime.now()}] Sent email to {receiver}")
    except Exception as e:
        print(f"[-] Error sending email: {e}")

def schedule_job():
    config = load_config()
    send_email(config)

if __name__ == "__main__":
    config = load_config()
    send_time = config.get("send_time", "09:00")
    schedule.every().day.at(send_time).do(schedule_job)
    print(f"[+] Scheduler started. Emails will be sent daily at {send_time}.")

    while True:
        schedule.run_pending()
        time.sleep(30)
