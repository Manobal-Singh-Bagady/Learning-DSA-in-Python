# ---------------- MSB's Coding Template ---------------- #
'''
    "ɴᴏ ᴄᴏᴅᴇ ɪꜱ ᴘᴇʀꜰᴇᴄᴛ"
'''

# ---I/O from file---#
import sys
try:
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
    sys.stderr = open("error.txt", "w")
except:
    pass


# ---------------------- Code Starts Here ----------------------#


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        if self.head is not None:
            self.tail.next = Node(value)  # type: ignore
            self.tail = self.tail.next  # type: ignore
        else:
            self.head = Node(value)
            self.tail = self.head

        self.length += 1
        return True


if __name__ == "__main__":
    my_linked_list = LinkedList(1)
    my_linked_list.make_empty()

    my_linked_list.append(1)
    my_linked_list.append(2)

    print('Head:', my_linked_list.head.value)  # type: ignore
    print('Tail:', my_linked_list.tail.value)  # type: ignore
    print('Length:', my_linked_list.length)

    print('\nLinked List:')
    my_linked_list.print_list()

    """
        EXPECTED OUTPUT:
        ----------------
        Head: 1
        Tail: 2
        Length: 2

        Linked List:
        1
        2
    """
