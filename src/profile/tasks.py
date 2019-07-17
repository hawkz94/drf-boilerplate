from celery_worker import app
from utils import notifications

@app.task
def send_sms(number, msg):
    print("Sending sms .....")
    notifications.send_sms(number, msg)

    return 'Send sms OK!'