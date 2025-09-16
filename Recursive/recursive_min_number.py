# Find the minimum value in a list using recursion
# Practice exercise from "Grokking Algorithms"

data = [1, 2, 3]


def find_min(arr):
    """Recursively find the minimum value in a list."""
    # Base case: if list has only one element, return it
    if len(arr) == 1:
        return arr[0]

    # Compare the first element with the minimum of the rest
    return arr[0] if arr[0] < find_min(arr[1:]) else find_min(arr[1:])


print(find_min(data))
