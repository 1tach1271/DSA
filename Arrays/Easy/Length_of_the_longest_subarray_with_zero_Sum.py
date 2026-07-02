# for 0
def s(arr,n):
    a =0
    l=0
    m={}
    for i in range(n):
        a+=arr[i]
        if a==0:
            l=i+1
        else:
            if a in m:
                l=max(l,i-m[a])
            else:
                m[a]=i
    print(l)
arr=list(map(int, input("Enter the array: ").split()))
n=len(arr)
s(arr,n)

# for k sum

def e(arr,n,k):
    a =0
    l=0
    m={}
    for i in range(n):
        a+=arr[i]
        if a==k:
            l=i+1
        if a-k in m:
            l=max(l,i-m[a-k])
        if a not in m:
            m[a]=i
    print(l)
arr=list(map(int, input("Enter the array: ").split()))
n=len(arr)
k =int(input("Enter the value of k: "))
e(arr,n,k)