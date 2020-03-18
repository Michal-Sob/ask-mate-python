from datetime import datetime
import bcrypt
from flask import session


def submission_time():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return now


def hash_password(plain_text_password):
    # By using bcrypt, the salt is saved into the hash itself
    hashed_bytes = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


def verify_password(plain_text_password, hashed_password):
    hashed_bytes_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_bytes_password)


def is_logged_in():
    logged_in = False
    if 'email' in session:
        logged_in = True
    return logged_in
