def median_followers(nums):
    nums = sorted(nums)
    length = len(nums)

    if length == 0:
        return None
        
    elif length % 2 != 0:
        return nums[length // 2]
        
    else:
        return (nums[length // 2] + nums[length // 2 - 1]) / 2
