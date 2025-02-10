nums = [5,7,7,8,8,8,10]
target = 8
i=0
if target not in nums:
    print("[-1,-1]")
else:
    indices = [i for i in range(len(nums)) if nums[i] == target]
    indices=[indices[0], indices[-1]]
    print(indices)




