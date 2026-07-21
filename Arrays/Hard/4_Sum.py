# 1.
def f(arr,n,c):
    s=set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if arr[i]+arr[j]+arr[k]+arr[l]==c:
                        a=tuple(sorted([arr[i],arr[j],arr[k],arr[l]]))
                        s.add(a)
    return [list(b) for b in s]
arr=list(map(int,input().split()))
n=len(arr)
c=int(input())
print(f(arr,n,c))

# 2.
