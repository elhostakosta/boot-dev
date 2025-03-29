def divide_list(nums, divisor):
    for i in range(0, len(nums)):
        nums[i] /= divisor
    return nums
