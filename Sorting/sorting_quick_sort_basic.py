# Quick Sort implementation
# Practice exercise from "Grokking Algorithms"

data = [2, 1, 0, 4]


def quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]

    low = [n for n in arr[1:] if n < pivot]
    high = [n for n in arr[1:] if n > pivot]

    print(f"Pivot: {pivot}")
    print(f"Low: {low}")
    print(f"High: {high}")

    return quick_sort(low) + [pivot] + quick_sort(high)


print(quick_sort(data))
