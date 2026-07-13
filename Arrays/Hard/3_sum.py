def f(arr,n):
    s=set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k]==0:
                    t=tuple(sorted([arr[i],arr[j],arr[k]]))
                    s.add(t)
    return [list(t) for t in s]
arr=list(map(int,input().split()))
n=len(arr)
print(f(arr,n))