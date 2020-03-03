from datetime import datetime

def submission_time():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return now
