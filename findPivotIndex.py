def pivotIndex(nums):
    totalValue = sum(nums)
    leftSumValue = 0
    for index, element in enumerate(nums):
        if leftSumValue == (totalValue - nums[index] - leftSumValue):
            return index
        else:
            leftSumValue += element
    return "-1"
