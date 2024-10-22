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
        self.head = Node(value)
        self.tail = self.head
        self.length = 1


if __name__ == "__main__":
    my_linked_list = LinkedList(4)

    print('Head:', my_linked_list.head.value)
    print('Tail:', my_linked_list.tail.value)
    print('Length:', my_linked_list.length)

    """
        EXPECTED OUTPUT:
        ----------------
        Head: 4
        Tail: 4
        Length: 1
    """
