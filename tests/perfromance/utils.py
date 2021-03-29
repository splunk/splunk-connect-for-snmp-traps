import os
import time

from datetime import datetime


def create_directory(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def get_current_date_time():
    now = datetime.now()
    print("now =", now)
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y-%H:%M:%S")
    print("date and time =", dt_string)
    return dt_string


def prepare_date_time_to_used_as_part_of_file_name(date_time):
    return date_time.replace("/", ".").replace(":", ".")

def save_data(name, data):
    # print(f"saving log for: {name}")
    log_file = open(name, "w+")
    log_file.write(f"{data}")


