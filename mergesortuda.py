def merge_sort(values):
    if len(values) <= 1:
        return values

    # split values into halves
    midpoint = len(values) // 2
    left_half = values[:midpoint]
    right_half = values[midpoint:]
    # recursive call on each half
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    # merge the sorted halves
    # loop and compare
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged = merged + [left[i]]
            i += 1
        else:
            merged = merged + [right[j]]
            j += 1

    # add the remaining elements to merged list
    merged += left[i:]
    merged += right[j:]

    return merged


test = [21, 4, 1, 3, 9, 392, 20, 25, 6, 21, 14]
result = merge_sort(test)
print(result)
