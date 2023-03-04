import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
sys.stderr = open("error.txt", "w")
# Comment the above 4 lines if you are not using file input output.


def add_items(a, b):
    return a+b


if __name__ == "__main__":
    print(add_items(10, 20))
