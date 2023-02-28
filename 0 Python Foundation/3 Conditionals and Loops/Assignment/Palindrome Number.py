n = int(input())

N = n
x = 0
while N > 0:
    x += N % 10*10**(len(str(N))-1)
    N //= 10
if n == x:
    print("True")
else:
    print("False")
