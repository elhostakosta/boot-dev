def find_max(nums):
    max = float("-Infinity")

    for num in nums:
        if num > max:
            max = num
    return max
