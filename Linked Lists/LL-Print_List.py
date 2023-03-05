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
        while temp != None:
            print(temp.value, end=' ')
            temp = temp.next
        print()

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # type: ignore
            self.tail = new_node
        self.length += 1
        return True


if __name__ == "__main__":
    my_linked_list = LinkedList(11)
    my_linked_list.append(3)
    my_linked_list.append(23)
    my_linked_list.append(7)

    my_linked_list.print_list()
