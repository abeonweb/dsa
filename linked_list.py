class Node:
    """
    an object for storing a single node of a linked list
    Models two attributes - data and a reference to the next node in the list
    """
    data = None
    next_node = None

    # constructor
    def __init__(self, data):
        self.data = data

    # representation of the node
    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:
    """
    Singly linked list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        """
        Takes O(n) time
        :return: count - the number of nodes in linkedlist
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """
        Adds a new node with data at head of the list
        Takes O(1)
        :param data:
        :return:
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, target):
        """
        search for the first data that matches the target
        Takes O(n)
        :param target:
        :return: the containing Node or None if not found
        """
        current = self.head

        while current:
            if current.data == target:
                return current

            current = current.next_node

        return None

    def insert(self, data, index):
        current = self.head

        if index == 0:
            self.add(data)

        if index > 0:
            new_node = Node(data)
            position = index

            while position > 1:
                current = current.next_node
                position -= 1

            new_node.next_node = current.next_node
            current.next_node = new_node

    def remove(self, key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current


    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1

            return current


    def __repr__(self):
        """
        Takes O(n) time
        :return: Returns a string representation of the list
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node

        return '-> '.join(nodes)
