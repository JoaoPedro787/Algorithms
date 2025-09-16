# Recursive search in a nested list
# Practice exercise from "Grokking Algorithms"

box = [
    42,
    7,
    99,
    [[13, 88, 5, [[72, 33], 61, 15, [[4, 56], 90, 38]]]],
    27,
    [81, [2, [44, 9, [100, [63, 47, [30, 54, [70, 11]]]]]]],
    [6, [95, [26, [50, [85, 21, [60, [18, 37, [79, [28, 65]]]]]]]]],
    48,
    12,
    [[25, 71], [87, [1, [93, [35, 59]]]]],
    [17, [[83, [76, [39, 91, [57, [10, 64]]]]]]],
    [14, [84, [[75, [31, [20, [45, [[23, [69, [36, [92]]]]]]]]]]]],
    19,
    [40, [55, [29, [62, [3, [68, [22]]]]]]],
    [73, [32, [8, [[97, [67, [24, [16, [98, [74]]]]]]]]]],
    41,
    53,
    [52, [[66, [82, [96, [34, [89, [49, [80, [58]]]]]]]]]],
    [46, [77, [94, [78, [86, [51, [43, [70]]]]]]]],
]

target = int(input("Enter a number to search: "))

attempts = 0
found = False


def search_box(arr):
    """Recursively search for the target inside a nested list."""
    global attempts, found

    print(f"Attempt {attempts} | Current array: {arr}")

    for item in arr:
        attempts += 1

        if item == target:
            found = True
            break
        elif isinstance(item, list) and not found:
            search_box(item)


search_box(box)

if found:
    print(f"\nFound the number {target}.")
else:
    print(f"\nDid not find the number {target}.")

print(f"\nTotal attempts: {attempts}")
