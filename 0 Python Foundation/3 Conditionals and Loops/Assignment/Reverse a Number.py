N = int(input())
r = 1 if N > 0 else -1
N *= r

x = 0
while N > 0:
    x += N % 10*10**(len(str(N))-1)
    N //= 10
print(x*r)
