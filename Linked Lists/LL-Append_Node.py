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

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)  # type: ignore
            self.tail = self.tail.next
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.value, end=' ')
            temp = temp.next
        print()


if __name__ == "__main__":
    new_list = LinkedList(1)
    new_list.append(2)
    new_list.append(3)
    new_list.print_list()
