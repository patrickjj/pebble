import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
def quick_sort(arr):
    stack = []
    stack.append((arr, 0, len(arr) - 1))

    while stack:
        arr, low, high = stack.pop()

        if low < high:
            pi = partition(arr, low, high)
            stack.append((arr, low, pi - 1))
            stack.append((arr, pi + 1, high))

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def timsort(arr):
    return sorted(arr)


def generate_random_array(size):
    return [random.randint(0, size) for _ in range(size)]

size = 10000

arr = generate_random_array(size)
start_time = time.time()
bubble_sort(arr)
end_time = time.time()
print("Bubble Sort took %.10f seconds" % (end_time - start_time))


start_time = time.time()
selection_sort(arr)
end_time = time.time()

print("Selection Sort took %.10f seconds" % (end_time - start_time))


start_time = time.time()
quick_sort(arr)
end_time = time.time()

print("Quick Sort took %.10f seconds" % (end_time - start_time))

start_time = time.time()
sorted_arr = timsort(arr)
end_time = time.time()
print("Timsort took %.10f seconds" % (end_time - start_time))