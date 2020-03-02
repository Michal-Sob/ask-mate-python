def submission_time():
    now = datetime.now()
    timestamp = round(datetime.timestamp(now))

    return timestamp
