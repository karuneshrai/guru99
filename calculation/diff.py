def diff(a,b):
    ans = a-b
    if ans > 0:
        return ans
    else:
        return 0
print('subtraction -> ',diff(1,2))