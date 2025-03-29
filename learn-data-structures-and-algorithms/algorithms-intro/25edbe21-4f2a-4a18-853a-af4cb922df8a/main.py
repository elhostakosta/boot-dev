def average_followers(nums):
    
    nums_count = len(nums)

    if nums_count == 0:
        return None
        
    sum = 0

    for num in nums:
        sum += num

    average = sum / nums_count
    return average
