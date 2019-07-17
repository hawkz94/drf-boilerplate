import boto3
from django.conf import settings

# Create an SNS client
client = boto3.client(
    "sns",
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name="us-east-1"
)


# Send your sms message.
def send_sms(number, msg):
    print("Sending sms ..... to {}".format(number))
    client.publish(
        PhoneNumber=number,
        Message=msg
    )