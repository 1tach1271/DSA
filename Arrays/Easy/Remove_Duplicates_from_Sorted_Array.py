def setss(arr,n):
    i=0
    for j in range(1,n):
        if arr[j]!=arr[i]:
            i+=1

            arr[i+1]=arr[j]
            
    
    print(arr[:i])
    return i+1
arr=list(map(int,input("enter the array ").split()))
n = len(arr)
print(setss(arr,n))