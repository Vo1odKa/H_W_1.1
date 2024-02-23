import time
from multiprocessing import Pool

def factorize(*nums):
    results = []
    for num in nums:
        factors = [i for i in range(1, num + 1) if num % i == 0]
        results.append(factors)
    return results

if __name__ == '__main__':
    numbers = [128, 255, 99999, 10651060]

    # Synchronous execution
    start_time_sync = time.time()
    results_sync = [factorize(num) for num in numbers]
    end_time_sync = time.time()
    print(f"Synchronous execution time: {end_time_sync - start_time_sync} seconds")

    # Asynchronous execution using multiprocessing Pool
    with Pool() as pool:
        start_time_async = time.time()
        results_async = pool.map(factorize, numbers)
        end_time_async = time.time()
        print(f"Parallel execution time: {end_time_async - start_time_async} seconds")

# Unpack the results correctly
a, b, c, d = factorize(128, 255, 99999, 10651060)

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
