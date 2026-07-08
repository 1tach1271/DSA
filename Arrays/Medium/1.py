def f(arr,n):
    if n==0:
        return 0
    l=1
    a=set()
    for i in range(n):
        a.add(arr[i])
    for i in a:
        if i-1 not in a:
            c=1
            b=i
            while b+1 in a:
                b+=1
                c+=1
            l=max(l,c)
    print(l)
arr=list(map(int,input().split()))
n=len(arr)
f(arr,n)