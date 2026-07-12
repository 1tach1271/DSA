# 1.
# def f(n):
#     for i in range(n):
#         print("*"*n,end="")
#         print()
# n=int(input())
# f(n)

# 2.
# def f(n):
#     for i in range(1,n+1):
#         if n%i==0:
#             print(i,end=" ")
# n=int(input())
# f(n)

# 3.
# def f(a,n,i):
#     if i>=n//2:
#         return True
#     if a[i]!=a[n-i-1]:
#         return False
#     return f(a,n,i+1)
# a=input()
# n=len(a)
# print(f(a,n,0))

# 4.
# from collections import defaultdict
# def f(arr,n):
#     h=defaultdict(int)
#     for i in range(n):
#         h[arr[i]]+=1
#     for a,b in h.items():
#         print(a,b)
# arr = list(map(int,input().split()))
# n=len(arr)
# f(arr,n)

# 5.
# def q(arr,low,high):
#     if low<high:
#         p = pa(arr,low,high)
#         q(arr,low,p-1)
#         q(arr,p+1,high)
# def pa(arr,low,high):
#     pivot = arr[low]
#     left = low 
#     right = high
#     while left<right:
#         while left<=high and arr[left]<=pivot:
#             left+=1
#         while right>= low and arr[right]>pivot:
#             right-=1
#         if left<right:
#             arr[left],arr[right]=arr[right],arr[left]
#     arr[right],arr[low]=arr[low],arr[right]
#     return right
# arr =list(map(int,input().split()))
# n=len(arr)
# q(arr,0,n-1)
# print(arr)

# 6.

# def f(arr,n):
#     a = float('-inf')
#     b= float('inf')
#     for i in range(n):
#         if arr[i]>a:
#             a=arr[i]
#         if arr[i]<b:
#             b=arr[i]
#     c = float('-inf')
#     d= float('inf')
#     e=c
#     f=d
#     for i in range(n):
#         if arr[i]>c and arr[i]!=a:
#             c=arr[i]
#         if arr[i]<d and arr[i]!=b:
#             d=arr[i]
#     if c == e:
#         c= -1
#     if d ==f:
#         d= -1
#     print("The second largest element is: ",c)
#     print("The second smallest element is: ",d)
# arr= list(map(int,input().split()))
# n = len(arr)
# f(arr,n)

# 6.
# def f(arr,n):
#     s= 0 
#     m= float('-inf')
#     a=0
#     b=-1
#     c=-1
#     for i in range(n):
#         if s==0:
#             a=i
#         s+=arr[i]
#         if s>m:
#             m=s
#             b=a
#             c=i
#         if s<0:
#             s=0
#     for i in range(b,c+1):
#         print(arr[i],end=" ")
# arr = list(map(int,input().split()))
# n=len(arr)
# f(arr,n)

