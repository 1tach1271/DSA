def m(arr,n):
    a=set(arr)
    for i in range(1,n+1):
        if i not in a:
            return i

arr=list(map(int,input().split()))
n=len(arr)+1
print(m(arr,n))