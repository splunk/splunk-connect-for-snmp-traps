import psutil
import os

def get_memory():
    # Getting % usage of virtual_memory ( 3rd field)
    print('RAM memory % used:', psutil.virtual_memory()[2])

def get_cpu_usage():
    # Calling psutil.cpu_precent() for 4 seconds
    print('The CPU usage is: ', psutil.cpu_percent(1))

def get_cpu_usage_2():
    # Getting loadover15 minutes
    load1, load5, load15 = psutil.getloadavg()
    cpu_usage = (load15 / os.cpu_count()) * 100
    print("The CPU usage is : ", cpu_usage)


if __name__ == "__main__":
    get_memory()
    get_cpu_usage_2()
    get_cpu_usage()
