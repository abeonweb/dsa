# divide and conquer
def mergesort(values):
    if len(values) <= 1:
        return values

    left, right = split(values)

    left_sort = mergesort(left)
    right_sort = mergesort(right)

    return merge(left_sort, right_sort)


def split(values):
    midpoint = len(values) // 2
    left_half = values[:midpoint]
    right_half = values[midpoint:]

    return left_half, right_half


def merge(left, right):
    merged = []
    l_index = 0
    r_index = 0

    while l_index < len(left) and r_index < len(right):
        if left[l_index] <= right[r_index]:
            merged.append(left[l_index])
            l_index += 1
        else:
            merged.append(right[r_index])
            r_index += 1

    # add whatever is left over
    merged = merged + left[l_index:]
    merged = merged + right[r_index:]

    return merged


test = [90, 34, 76, 45, 12, 0, 34, 19]
result = mergesort(test)
print(result)
