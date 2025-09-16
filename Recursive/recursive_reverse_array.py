# Reverse a list using recursion
# Practice exercise from "Grokking Algorithms"

data = [10, 7, 4, 8, 1]


def reverse_list(arr):
    """Recursively reverse a list."""
    if arr == []:
        return []

    # Take the last element and append the reverse of the rest
    return [arr[-1], *reverse_list(arr[:-1])]


print(reverse_list(data))
