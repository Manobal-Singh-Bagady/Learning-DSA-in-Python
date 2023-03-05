import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
sys.stderr = open("error.txt", "w")
# Comment the above 4 lines if you are not using file input output.


class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


if __name__ == "__main__":

    cookie_one = Cookie('green')
    cookie_two = Cookie('blue')

    print('Cookie one is', cookie_one.get_color())
    print('Cookie two is', cookie_two.get_color())

    cookie_one.set_color('yellow')

    print('\nCookie one is now', cookie_one.get_color())
    print('Cookie two is still', cookie_two.get_color())
