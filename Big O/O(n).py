import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
sys.stderr = open("error.txt", "w")
# Comment the above 4 lines if you are not using file input output.


def print_items(n):
    for i in range(n):
        print(i)


if __name__ == "__main__":
    print_items(10)
