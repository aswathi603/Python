import time 
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool

def cpu_task(power):
    count =0
    for i in range(10**power):
        count += 1
    return count


if __name__ == "__main___":
    num_tasks = 5 
    power =7

    print("Comparing Multithreading Vs. Multiprocessing (CPU-Bound Task)")


    ##MultiThreading
    start_time_thread = time.time()
    with ThreadPoolExecutor(max_workers=num_tasks) as executor:
        result_thread = list(executor.map(cpu_task, [power]*num_tasks))
    end_time_thread = time.time()
    time_taken_thread = end_time_thread - start_time_thread
    print(f"Multithreading Time Taken: {time_taken_thread:.4f} seconds")
    print(f"Thread Results (first few) : {result_thread[:2]}\n")



    ##MultiProcessing
    start_time_process =time.time()
    with Pool(processes=num_tasks) as pool:
        result_process = list(pool.map(cpu_task, [power]*num_tasks))
    end_time_process =time.time()
    time_taken_process = end_time_process - start_time_process
    print(f"Multitprocessing Time Taken: {time_taken_process:.4f} seconds")
    print(f"Process Result(first few) : {result_process}\n")


    print("Comparision:")
    if time_taken_process < time_taken_thread:
        speedUp =time_taken_thread/time_taken_process
        print(f"Multiprocessing was significantly faster , achieving a speedup of {speedup:.2f}x.")
    elif time_taken_thread< time_taken_process:
        slowDown= time_taken_process/time_taken_thread
        print(f"Multiprocessing was slower by a factor of {slowDown:.2f}x.")
    else:
        print("Multithreading and Multiprocessing performance was similar.")