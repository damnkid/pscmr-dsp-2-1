# Linear Search Program
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Main Program
arr = [34, 7, 23, 32, 5, 62]
target = int(input("Enter the element to search: "))
index = linear_search(arr, target)

if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found in the list.")
