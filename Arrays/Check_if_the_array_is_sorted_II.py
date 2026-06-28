def pattern(arr,n):
    a=[]
    for i in range(1,n):
        if arr[i-1]>arr[i]:
            print("not sorted")
            return
    print("sorted")


arr=list(map(int,input().split()))
pattern(arr,len(arr))