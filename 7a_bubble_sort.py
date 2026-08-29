# Bubble Sort Program
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to detect if any swapping happens
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped in inner loop, break
        if not swapped:
            break


arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
bubble_sort(arr)
print("Sorted array:", arr)
