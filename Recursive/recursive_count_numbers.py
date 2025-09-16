# Count the number of elements in a list using recursion
# Practice exercise from "Grokking Algorithms"

data = [1, 2, 3, 4, 5]


def count_elements(arr):
    """Recursively count the number of elements in a list."""
    if arr == []:
        return 0
    return 1 + count_elements(arr[1:])


print(count_elements(data))
