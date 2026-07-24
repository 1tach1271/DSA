from collections import defaultdict
def f(arr,n):
    s=0
    m=0
    h=defaultdict(int)
    for i in range(n):
        s+=arr[i]
        if s==0:
            m=i+1
        if s!=0:
            if s in h:
                m=max(m,i-h[s])
            else:
                h[s]=i
    print(m)           
arr=list(map(int,input().split()))
n=len(arr)
f(arr,n)