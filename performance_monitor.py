import psutil 
import time
import algorithms

def measure_performance(algorithm, *args):
    start_time = time.time()

    start_memory = psutil.Process().memory_info().rss

    res = algorithm(*args)

    end_memory = psutil.Process().memory_info().rss

    execution_time = time.time() - start_time

    mb_used = (end_memory - start_memory) / (1024**2)

    return res, execution_time, mb_used