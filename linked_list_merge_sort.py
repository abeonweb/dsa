from linked_list import LinkedList


def merge_sort(linked_list):
    """
    Sorts a linkedList in ascending order
    - Recursively divide the linked list into sublist of a single list
    - Repeatedly merge the sublist to produce sorted sublist until one remains
    :param linked_list:
    :return: Returns a sorted linked list
    Takes O(kn log n)
    """
    # stopping condition
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(linked_list):
    """
    Divide the unsorted list at midpoint into two sublist
    Take Big O(k log n)
    param linked_list:
    :return:
    """

    if linked_list is None or linked_list.head is None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2

        mid_node = linked_list.node_at_index(mid - 1)  # index is one less

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half


def merge(left, right):
    """
    Merges two linked list sorting by data in the node
    Take O(n) time
    :param left:
    :param right:
    :return: a new merged list
    """

    # create a new linked list that contains nodes from merging left and right
    merged = LinkedList()

    # add a fake head that is discarded later
    merged.add(0)

    # Set current to the head of the linked list
    current = merged.head

    # Obtain head node for left and right linked lists
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach the first tail node
    while left_head or right_head:
        # if the head node of left is None, we are past the tail
        # Add the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            # Call next on right to set loop condition to false
            right_head = right_head.next_node
        # if the head node of right is None, we are past the tail
        # Add the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            # Call next on left to set loop condition to false
            left_head = left_head.next_node
        else:
            if left_head.data < right_head.data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node
        # move current to next position after every iteration
        current = current.next_node
    # Discard fake head by assigning next node as head
    merged.head = merged.head.next_node
    return merged


link_list = LinkedList()
link_list.add(10)
link_list.add(2)
link_list.add(44)
link_list.add(15)
link_list.add(200)

print(link_list)
sorted_linked_list = merge_sort(link_list)
print(sorted_linked_list)
