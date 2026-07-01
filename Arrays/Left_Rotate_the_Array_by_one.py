def r(nums, n):
    for i in range(1,n-1):
        nums[i-1],nums[i]=nums[i],nums[i-1]
    nums[n-1],nums[n-2]=nums[n-2],nums[n-1]
    print(nums)
nums = list(map(int,input().split()))
n = len(nums)
r(nums,n)