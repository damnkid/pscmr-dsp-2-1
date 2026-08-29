# Binary Search Program
# Note: Array must be sorted
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# Main Program
arr = [5, 7, 23, 32, 34, 62]  # Sorted array
target = int(input("Enter the element to search: "))
index = binary_search(arr, target)

if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found in the list.")
