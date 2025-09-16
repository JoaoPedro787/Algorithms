# Count the number of even numbers in a list using recursion
# Practice exercise from "Grokking Algorithms"

data = [1, 2, 4]


def count_even(arr):
    """Recursively count the number of even numbers in a list."""
    print(arr)  # Show the current state of the array

    if arr == []:
        return 0

    # Check if the first element is even, then add the count from the rest
    return (1 if arr[0] % 2 == 0 else 0) + count_even(arr[1:])


print(count_even(data))
