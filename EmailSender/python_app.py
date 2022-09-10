# email 보내는데 필요한 모듈 가져오기
from email.message import EmailMessage
from app2 import password
import ssl
import smtplib

# 이메일 보내는 사람
email_sender = "chosangho2019@gmail.com"
# 이메일 패스워드
email_password = password
# 이메일 받는 사람
email_receiver = "teha007@naver.com"

# 이메일 제목 
subject = "HI SANGHO"

# 이메일 본문 내용
body = """
  Email send to sangho
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
