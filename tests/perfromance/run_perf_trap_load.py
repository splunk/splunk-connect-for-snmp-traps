import time
import config
import utils
# from metrics import Metrics

from perf_engine import start_many_threads, start_many_processes
from send_trap import send_trap_loop

if __name__ == "__main__":
    print("here we go!")
    threads_list = []
    threads_number = config.threads_number

    start_time = time.time()
    # start_many_threads(threads_list, threads_number, send_trap_loop)
    sum_of_traps = start_many_processes(threads_list, threads_number, send_trap_loop)
    end_time = time.time()
    print("END")

    # sum_of_traps = 0
    # for x in Metrics.how_many_events:
    #     sum_of_traps = Metrics.how_many_events
    # print(f"how_many_events: {Metrics.how_many_events}")
    print(f"Ile Trapow: {sum_of_traps}, execution time: {(end_time - start_time)}")
    print(f"Ile na sec: {sum_of_traps / (end_time - start_time)}")
