def bubble_sort(array):
    """
    the Big O = O(n^2)
    :param array:
    :return: a sorted array
    """
    for i in range(len(array)):
        for j in range(len(array)):
            if j + 1 < len(array) and array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

    return array



items = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]

print(bubble_sort(items))
