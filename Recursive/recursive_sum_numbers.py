# Sum all elements in a list using recursion
# Practice exercise from "Grokking Algorithms"

data = [1, 2, 3, 4, 5]


def recursive_sum(arr):
    """Recursively sum all elements in a list."""
    if arr == []:
        return 0  # Base case: empty list

    return arr[0] + recursive_sum(arr[1:])


print(recursive_sum(data))
