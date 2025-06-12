def heapify(arr, n, i):
    largest = i           # Initialize largest as root
    left = 2 * i + 1       # left child index
    right = 2 * i + 2      # right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and heapify the affected subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    # Step 1: Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Swap current root with end
        arr[0], arr[i] = arr[i], arr[0]
        # Heapify reduced heap
        heapify(arr, i, 0)

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
heapsort(arr)
print("Sorted array:", arr)


import random
import time
import copy
import sys

# Increase recursion limit for large inputs
sys.setrecursionlimit(10000)

# Heapsort Implementation
def heapsort(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[l] > arr[largest]: largest = l
        if r < n and arr[r] > arr[largest]: largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# Mergesort Implementation
def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergesort(L)
        mergesort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Quicksort Implementation with Random Pivot
def quicksort(arr):
    def _quicksort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            _quicksort(arr, low, pi - 1)
            _quicksort(arr, pi + 1, high)

    def partition(arr, low, high):
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Random pivot
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    _quicksort(arr, 0, len(arr) - 1)

# Function to run timing tests
def run_test(n, distribution):
    base = {
        "random": [random.randint(0, 1000000) for _ in range(n)],
        "sorted": list(range(n)),
        "reverse": list(range(n, 0, -1))
    }[distribution]

    times = {}
    for name, sort_fn in [("Heapsort", heapsort), ("Mergesort", mergesort), ("Quicksort", quicksort)]:
        arr = copy.deepcopy(base)
        start = time.time()
        sort_fn(arr)
        end = time.time()
        times[name] = round(end - start, 4)
    return times

# Main block to run the tests
if __name__ == "__main__":
    print("Starting Heapsort vs Mergesort vs Quicksort comparison...\n")
    sizes = [1000, 10000, 100000]  # You can modify or add sizes here
    distributions = ["random", "sorted", "reverse"]

    for size in sizes:
        print(f"\nArray size: {size}")
        for dist in distributions:
            print(f"  Input type: {dist}")
            try:
                results = run_test(size, dist)
                for algo, t in results.items():
                    print(f"    {algo}: {t:.4f} seconds")
            except Exception as e:
                print(f"    Error: {e}")
