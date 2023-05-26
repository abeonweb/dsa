def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    # select any value to use to divide the list in two
    pivot = arr[len(arr) - 1]
    # best results come from picking pivot at random
    lesser_values = []
    greater_values = []

    for val in arr[: len(arr) - 1]:
        if val < pivot:
            lesser_values.append(val)
        else:
            greater_values.append(val)
    # call quicksort recursively
    lesser_sorted = quick_sort(lesser_values)
    greater_sorted = quick_sort(greater_values)
    print("%25s %1s %-25s" %(lesser_sorted, pivot, greater_sorted))
    return lesser_sorted + [pivot] + greater_sorted


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quick_sort(test))

