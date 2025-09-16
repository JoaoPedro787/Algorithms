# Iterative binary search in a sorted list
# Practice exercise from "Grokking Algorithms"

# Create a list from 1 to 100
arr = [n for n in range(1, 101)]

target = 35  # Number we want to find


def binary_search():
    """Perform an iterative binary search on a sorted list."""
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        print(f"Value in array: {arr[mid]}, target value: {target}")

        if arr[mid] == target:
            print("Found it!")
            return
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1


binary_search()
