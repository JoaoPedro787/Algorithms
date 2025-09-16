# Check if a value exists in a list using recursion
# Practice exercise from "Grokking Algorithms"

data = [2, 5, 9]
target = 9


def contains(arr):
    """Recursively check if the target exists in the list."""
    if arr == []:
        return False

    return True if arr[0] == target else contains(arr[1:])


print(contains(data))
