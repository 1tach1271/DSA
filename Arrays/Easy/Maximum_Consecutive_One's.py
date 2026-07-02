def f(arr,n):
    a=0
    b=0
    for i in range(0,n):
        if arr[i]==1:
            a+=1
        else:
            a=0
        b=max(b,a)
    print(b)
arr=list(map(int,input().split()))
n=len(arr)
f(arr,n)