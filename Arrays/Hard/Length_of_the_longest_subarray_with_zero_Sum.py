def f(arr,n):
    s=0
    l=0
    a={}
    for i in range(n):
        s+=arr[i]
        if s==0:
            l=i+1
        elif s in a:
            l = max(l,i-a[s])
        else:
            a[s]=i 
    print(l)
arr=list(map(int,input().split()))
n=len(arr)
f(arr,n)