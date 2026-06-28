def quick_sort(arr,low, high):
    if (low<high):
        pivotindex = partition(arr,low,high)
        quick_sort(arr,low, pivotindex-1)
        quick_sort(arr,pivotindex+1,high)
def partition(arr, low, high):
    pivot = arr[low]
    i =low
    j= high
    while i<j:
        while i<=high and arr[i]<=pivot :
            i+=1
        while  j>=low and arr[j]>pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[low], arr[j]=arr[j],arr[low]
    return j
arr  = list(map(int,input("Enter the array: ").split()))
n = len(arr)
quick_sort(arr,0,n-1)
print(arr)