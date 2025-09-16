# Find the maximum depth of a nested list
# Practice exercise from "Grokking Algorithms"

data = [
    10,
    [5, [2, [8, 1], 3], 7],
    [[4, 6], [9, [11, [13]]]],
    20,
    [[[15]], 25, [30, [40, [50]]]],
    [],
]

max_depth = 1  # Global variable to store maximum depth


def find_max_depth(arr, depth):
    """Recursively find the maximum depth of a nested list."""
    global max_depth

    if depth > max_depth:
        max_depth = depth

    for item in arr:
        if isinstance(item, list):
            find_max_depth(item, depth + 1)


find_max_depth(data, 1)

print(max_depth)
