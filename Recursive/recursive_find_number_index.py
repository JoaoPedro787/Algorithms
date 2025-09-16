# Find the index of a value in a list using recursion
# Practice exercise from "Grokking Algorithms"

data = [1, 2, 3]
target = 3


def find_index(arr):
    """Recursively find the index of the target in a list."""
    print(arr)  # Show the current state of the array

    if arr == []:
        return -1  # Value not found

    if arr[0] == target:
        return 0  # Found at the first position

    idx = find_index(arr[1:])  # Search in the rest of the list

    # If found in the rest, add 1 to adjust the index
    return -1 if idx < 0 else idx + 1


print(find_index(data))
