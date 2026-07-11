from collections import defaultdict
def f(arr,n,k):
    h=defaultdict(int)
    ps=0
    c=0
    h[0]=1
    for i in range(n):
        ps+=arr[i]
        a=ps-k
        if a in h:
            c+=h[a]
        h[ps]=h.get(ps,0) +1
    print(c)
arr=list(map(int,input().split()))
k=int(input())
n=len(arr)
f(arr,n,k)