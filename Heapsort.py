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
