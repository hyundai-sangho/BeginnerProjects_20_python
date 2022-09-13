# pip install schedule
# pip install requests
# from credentials import mobile_number
import requests
import schedule
import time


def send_message():
    resp = requests.post(
        "https://textbelt.com/text",
        {"phone": "010-8711-2138", "message": "Hey, Good morning", "key": "textbelt"},
    )

    print(resp.json())


# schedule.every().dat.at("06:00").do(send_message)

schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
