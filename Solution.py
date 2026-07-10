# def f(n):
#     for i in range(n,0,-1):
#         print("*"*i,end="")
#         print()
# n=int(input())
# f(n)

# def a(n):
#     l=0
#     m=0
#     while n>0:
#         l=n%10
#         m=m*10 + l
#         n=n//10
#     print(m)
# n=int(input())
# a(n)

# def f(n,c):
#     if c>n:
#         return 
#     print(c,end=" ")
#     f(n,c+1)
# n=int(input())
# f(n,1)

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

# def f(arr,n):
#     if n==1:
#         return
#     for j in range(n-1):
#         if arr[j+1]<arr[j]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
#     f(arr,n-1)
# arr=list(map(int,input().split()))
# n=len(arr)
# f(arr,n)
# print(arr)

# def f(arr,n):
#     x=0
#     for i in range(n):
#         x=x^arr[i]
#     print(x)
# arr=list(map(int,input().split()))
# n=len(arr)
# f(arr,n)

# def f(arr,n):
#     a=[]
#     b=[]
#     for i in range(n):
#         if arr[i]>0:
#             a.append(arr[i])
#         else:
#             b.append(arr[i])
#     j=0
#     s=0
#     for i in range(n):
#         if i%2==0:
#             arr[i]=a[j]
#             j+=1
#         else:
#             arr[i]=b[s]
#             s+=1
# arr=list(map(int,input().split()))
# n=len(arr)
# f(arr,n)
# print(arr)

# def f(arr,n):
#     a=[0]*n
#     b=0
#     c=1
#     for i in range(n):
#         if arr[i]<0:
#             a[c]=arr[i]
#             c+=2
#         else:
#             a[b]=arr[i]
#             b+=2
#     print(a)
# arr=list(map(int,input().split()))
# n=len(arr)
# f(arr,n)