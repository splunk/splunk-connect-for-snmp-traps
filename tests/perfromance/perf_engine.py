import time
from threading import Thread
from multiprocessing import Process, Value
import config
import utils


def start_many_threads(threads_list, number_of_threads_to_start, scenario_name_to_run):
    how_long_to_run_sec = 10

    for x in range(number_of_threads_to_start):
        print(f"Starting Thread: {x}")
        new_thread = Thread(target=scenario_name_to_run, args=(how_long_to_run_sec, f"Thread-{x}"))
        new_thread.start()
        threads_list.append(new_thread)
        # time.sleep(1)  # delay between Threads

    for current_thread in threads_list:
        current_thread.join()
    print(f"Waiting for Threads to finish")


def start_many_processes(threads_list, number_of_threads_to_start, scenario_name_to_run):
    how_long_to_run_sec = config.how_long_to_run_sec
    shared_value = Value('i', 0)
    # y = Value('i', 0)
    dt = utils.get_current_date_time()
    log_directory = "./logs/" + utils.prepare_date_time_to_used_as_part_of_file_name(dt) + "/"
    print(log_directory)

    utils.create_directory(log_directory)

    for x in range(number_of_threads_to_start):
        print(f"Starting Thread-{x}")
        new_thread = Process(target=scenario_name_to_run, args=(shared_value, log_directory, how_long_to_run_sec, f"Thread-{x}"))
        new_thread.start()
        threads_list.append(new_thread)
        # time.sleep(0.2)  # delay between Threads

    for current_thread in threads_list:
        current_thread.join()

    print(f"Waiting for Threads to finish")
    print(f"SHARED: {shared_value}")
    return shared_value.value
