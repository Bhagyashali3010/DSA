nums = [1,0,0,3,5]
count=0
# for i in range(len(nums)):
#     if 0 in nums:
#         nums.remove(0)
# x=min(nums)
# print(x, nums)
while sum(nums)!=0:
    for i in range(len(nums)):
        if 0 in nums:
            nums.remove(0)
    x=min(nums)
    for j in range (len(nums)):
        nums[j]-=x
    count+=1
    print(x, nums,count)
    