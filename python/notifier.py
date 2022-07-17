import time
from plyer import notification

# notifier
while True:
    notification.notify (
        title = "ALERT!!!",
        message = "Please do your studies.",
        timeout = 60
    )
    time.sleep(1800) # 30min