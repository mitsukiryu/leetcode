def twoSum(nums, target):
    my_dict = {}
    for i in range(len(nums)):
        my_dict[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in my_dict and my_dict[complement] != i:
            return [i, my_dict[complement]]
    return []


print(twoSum([3, 2, 4], 6))
