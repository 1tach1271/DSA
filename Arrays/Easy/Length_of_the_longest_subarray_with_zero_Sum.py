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