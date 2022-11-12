def runningSum(nums):
    for element in range(1, len(nums)):
        nums[element] += nums[element-1]
    return nums
