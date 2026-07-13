# 1.
# def f(n):
#     for i in range(n):
#         if i%2==0:
#             val=1
#         else:
#             val=0
#         for j in range(i+1):
#             print(val,end=" ")
#             val=1-val
#         print()
# n=int(input())
# f(n)

# 2.
# def f(a,b):
#     while a>0 and b>0:
#         if a>b:
#             a-=b
#         else:
#             b-=a
#     if a==0:
#         print(b)
#     else:
#         print(a)
# a=int(input())
# b=int(input())
# f(a,b)

# 3.
# def f(arr):
#     arr[:]=arr[::-1]
#     print(arr)
# arr = list(map(int,input().split()))
# f(arr)

# 4.
# from collections import defaultdict
# def f(arr,n):
#     h=defaultdict(int)
#     for i in range(n):
#         h[arr[i]]+=1
#     for a,b in h.items():
#         print(a,b)
# arr=list(map(int,input().split()))
# n=len(arr)
# f(arr,n)

# 5.
# def b(arr,n):
#     if n==1:
#         return
#     for j in range(n-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
#     b(arr,n-1)
# arr=list(map(int,input().split()))
# n=len(arr)
# b(arr,n)
# print(arr)

# 6.
# def pattern(arr,n):
#     if n<2:
#         return -1
#     a = arr[0]
#     b = float('inf')
#     a1 = arr[0]
#     b1 = float('inf')
#     for i in range(0,n):
#         if a < arr[i]:
#             a=arr[i]
#         if b > arr[i]:
#             b=arr[i]
#     for i in range(0,n):
#         if a1< arr[i] and arr[i]!=a:
#             a1 = arr[i]
#         if b1 > arr[i] and arr[i]!=b:
#             b1 = arr[i]
#     print(a1)
#     print(b1)

# arr = list(map(int, input().split()))
# pattern(arr, len(arr))        

# 7.
# def f(arr,n):
#     low=0
#     mid=0
#     high=n-1
#     while mid<=high:
#         if arr[mid]==0:
#             arr[mid],arr[low]=arr[low],arr[mid]
#             low+=1
#             mid+=1
#         elif arr[mid]==1:
#             mid+=1
#         else:
#             arr[mid],arr[high]=arr[high],arr[mid]
#             high-=1
#     print(arr)
# arr=list(map(int,input().split()))
# n=len(arr)
# f(arr,n)