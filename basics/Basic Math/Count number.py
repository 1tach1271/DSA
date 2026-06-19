def pattern(num):
    c=0
    while num>0:
        c=c+1
        num = num//10
    return c
num = int(input())
print(pattern(num))