import math


def getSecondOrderElements(n: int, a: [int]) -> [int]:
    s_mx = -math.inf
    mx = -math.inf

    s_mn = math.inf
    mn = math.inf

    for i in a:
        if i > mx:
            s_mx = mx
            mx = i

        if i > s_mx and i != mx:
            s_mx = i

        if i < mn:
            s_mn = mn
            mn = i

        if i < s_mn and i != mn:
            s_mn = i

    return [s_mx, s_mn]


num = int(input())
lst = list(map(int, input().split()))

print(*getSecondOrderElements(num, lst))
