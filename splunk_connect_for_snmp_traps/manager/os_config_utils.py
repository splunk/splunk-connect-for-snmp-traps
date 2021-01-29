from multiprocessing import cpu_count


# This function is used to get the optimal number of threads that should be used by
# a ThreadPoolExecutor. Using more threads than the number of HW threads, does not
# make sense.
def max_allowed_working_threads(suggested_user_value):
    total_cpu_cores = cpu_count()
    return suggested_user_value if suggested_user_value < total_cpu_cores else total_cpu_cores
