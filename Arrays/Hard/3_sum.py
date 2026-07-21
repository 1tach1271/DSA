# 1.
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

# 2.
def f(arr,n):
    s=set()
    for i in range(n):
        a=set()
        for j in range(i+1,n):
            c=-(arr[i]+arr[j])
            if c in a:
                d=tuple(sorted([arr[i],arr[j],c]))
                s.add(d)
            a.add(arr[j])
    return [list(d) for d in s]
arr=list(map(int,input().split()))
n=len(arr)
print(f(arr,n))

# 3.
def f(arr,n):
    arr.sort()
    a=[]
    for i in range(n):
        if i>0 and arr[i]==arr[i-1]:
            continue
        left=i+1
        right = n-1
        while left<right:
            s=arr[i]+arr[left]+arr[right]
            if s==0:
                a.append([arr[i],arr[left],arr[right]])
                left+=1
                right-=1
                while left<right and arr[left]==arr[left-1]:
                    left+=1
                while left<right and arr[right]==arr[right+1]:
                    right-=1
            elif s<0:
                left+=1
            else:
                right-=1
    return a
arr=list(map(int,input().split()))
n=len(arr)
print(f(arr,n))