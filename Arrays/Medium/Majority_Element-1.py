from collections import defaultdict
# 1.
def p(arr,n):
    m=defaultdict(int)
    for i in range(n):
        m[arr[i]]+=1
    a= n//2
    for i in m:
        if m[i]>a:
            return i
arr = list(map(int,input("Enter the array: ").split()))
n = len(arr)
print(p(arr,n))

# 2.
def s(arr,n):
    count = 0
    for i in range(n):
        if count==0:
            count+=1
            a=arr[i]
        elif arr[i]==a:
            count+=1
        else:
            count-=1
    c1=0
    for i in range(n):
        if arr[i]==a:
            c1+=1
    if c1>n//2:
        return a
    return -1
arr=list(map(int,input("Enter the array: ").split()))
n = len(arr)
print(s(arr,n))