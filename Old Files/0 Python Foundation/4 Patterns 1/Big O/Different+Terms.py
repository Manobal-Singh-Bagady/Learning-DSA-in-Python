import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
sys.stderr = open("error.txt", "w")
# Comment the above 4 lines if you are not using file input output.


def print_items(a, b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)


if __name__ == "__main__":
    print_items(1, 10)
