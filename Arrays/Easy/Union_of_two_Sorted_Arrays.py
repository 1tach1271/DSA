1.

from collections import defaultdict
def p(arr,n,arr2,m):
    hash = defaultdict(int)
    for i in range(n):
        hash[arr[i]]+=1
    for i in range(m):
        hash[arr2[i]]+=1
    for a in hash.keys():
        print(a)
arr = list(map(int,input().split()))
n = len(arr)
arr2 = list(map(int,input().split()))
m = len(arr2)
p(arr,n,arr2,m)

2.

def s(arr1,arr2,n,m):
    a=set()
    a=a.union(arr1)
    a=a.union(arr2)
    print(a)
arr1 = list(map(int,input().split()))
n = len(arr1)
arr2 = list(map(int,input().split()))
m = len(arr2)
s(arr1,arr2,n,m)

3.

def s(arr1,arr2,n,m):
    a=[]
    i,j=0,0
    while i<n and j<m:
        if arr1[i]<arr2[j]:
            if not a or a[-1]!=arr1[i]:
                a.append(arr1[i])
            i+=1
        elif arr2[j]<arr1[i]:
            if not a or a[-1]!=arr2[j]:
                a.append(arr2[j])
            j+=1
        else:
            if not a or a[-1]!=arr1[i]:
                a.append(arr1[i])
            i+=1
            j+=1
    while i<n:
        if not a or a[-1]!=arr1[i]:
            a.append(arr1[i])
        i+=1
    while j<m:
        if not a or a[-1]!=arr2[j]:
            a.append(arr2[j])
        j+=1
    print(a)
arr1 = list(map(int,input().split()))
n = len(arr1)
arr2 = list(map(int,input().split()))
m = len(arr2)
s(arr1,arr2,n,m)