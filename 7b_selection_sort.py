# Selection Sort Program
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the current index is the minimum
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Main Program
arr = [29, 10, 14, 37, 13]
print("Original array:", arr)
selection_sort(arr)
print("Sorted array:", arr)
