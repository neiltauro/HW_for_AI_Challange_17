import time
import random
import matplotlib.pyplot as plt

def systolic_bubble_sort(arr):
    N = len(arr)
    for _ in range(N - 1):
        for i in range(N - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

sizes = [10, 100, 1000, 3000]  # You can add 10000 if your machine can handle it
times = []

for size in sizes:
    data = [random.randint(0, size) for _ in range(size)]
    start_time = time.time()
    systolic_bubble_sort(data)
    end_time = time.time()
    exec_time = end_time - start_time
    times.append(exec_time)
    print(f"Sorted {size} elements in {exec_time:.5f} seconds")

plt.plot(sizes, times, marker='o')
plt.xlabel('Input Size (N)')
plt.ylabel('Execution Time (seconds)')
plt.title('Systolic Bubble Sort Execution Time')
plt.grid(True)
plt.show()
