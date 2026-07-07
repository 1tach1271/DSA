# 1. Permutation

def f(arr,idx):
    if idx==n:
        print(arr)
        return
    for i in range(idx,n):
        arr[i],arr[idx]=arr[idx],arr[i]
        f(arr,idx+1)
        arr[idx],arr[i]=arr[i],arr[idx]
arr=list(map(int,input().split()))
n=len(arr)
f(arr,0)

# 2.
from itertools import permutations
def f(arr,n):
    a = sorted(set(permutations(arr)))
    c=len(a)
    b=tuple(arr)
    for i in range(c):
        if a[i]==b:
            if i==c-1:
                return list(a[0])
            return list(a[i+1])
arr=list(map(int,input().split()))
n=len(arr)
print(f(arr,n))

# 3.
def f(arr,n):
    idx = -1
    for i in range(n-2,-1,-1):
        if arr[i]<arr[i+1]:
            idx=i
            break
    if idx==-1:
        arr[:]=reversed(arr[:])
        return arr
    for i in range(n-1,idx,-1):
        if arr[i]>arr[idx]:    
            arr[i],arr[idx]=arr[idx],arr[i]
            break
    arr[idx+1:]=reversed(arr[idx+1:])
    return arr

arr=list(map(int,input().split()))
n=len(arr)
print(f(arr,n))