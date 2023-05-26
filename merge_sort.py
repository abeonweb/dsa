def merge_sort(list):
    """
    sorts the given list in ascending order

    Divide: find the midpoint of the list and divide into sublist
    Conquer: recursively sort the sub-lists created in previous step
    Combine: merge the sorted sublist created in previous step
    :param list:
    :return: returns a new sorted list

    the overall is O(n log n) because of the merge and split methods
    """
    # stop case is an empty or one element list
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    divide the unsorted list at midpoint into sub-lists
    :param list:
    :return: two sub-lists

    Takes O(log n) time
    """

    mid = len(list)//2
    left = list[:mid] #mid not included
    right = list[mid:]

    return left, right


def merge(left, right):
    """
    merges two list/ arrays sorting them in the process
    :param left:
    :param right:
    :return: returns a new list

    Takes O(n) overall.
    """
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])


alist = [98, 22, 67, 10, 76, 34, 91, 45, 18]
l = merge_sort(alist)
print(verify_sorted(alist))
print(verify_sorted(l))