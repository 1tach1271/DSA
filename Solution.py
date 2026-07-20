# 1.
# def f(n):
#     for i in range(n-1,-1,-1):
#         for j in range(i+1):
#             print(chr(65+j),end=" ")
#         print()
# n=int(input())
# f(n)

# 2.
# def p(n):
#     a=n
#     l=0
#     m=0
#     while a>0:
#         l=a%10
#         m=m*10+l
#         a=a//10
#     if m==n:
#         print("Palindrome")
#     else:
#         print("Not palindrome")
# n=int(input())
# p(n)

# 3.
# def r(n,m):
#     if m>n:
#         return
#     print(m,end=" ")
#     r(n,m+1)
# n=int(input())
# r(n,1)

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
# def i(arr,n):
#     for i in range(1,n):
#         j=i
#         while j>0 and arr[j-1]>arr[j]:
#             arr[j],arr[j-1]=arr[j-1],arr[j]
#             j-=1
# arr=list(map(int,input().split()))
# n=len(arr)
# i(arr,n)
# print(arr)

# 6.
# def z(arr,n):
#     a=[0]*n
#     b=0
#     for i in range(n):
#         if arr[i]!=0:
#             a[b]=arr[i]
#             b+=1
#     print(a)
# arr=list(map(int,input().split()))
# n=len(arr)
# z(arr,n)

# def z(arr,n):
#     a=-1
#     for i in range(n):
#         if arr[i]==0:
#             a=i
#             break
#     if a==-1:
#         return arr
#     for i in range(a+1,n):
#         if arr[i]!=0:
#             arr[i],arr[a]=arr[a],arr[i]
#             a+=1
#     return arr
# arr=list(map(int,input().split()))
# n=len(arr)
# print(z(arr,n))

# 7.
# def f(arr,n):
#     m=1
#     for i in range(n):
#         b=1
#         a=arr[i]
#         while a+1 in arr:
#             b+=1
#             a+=1
#             m=max(m,b)
#     print(m)
# arr=list(map(int,input().split()))
# n=len(arr)
# f(arr,n)

