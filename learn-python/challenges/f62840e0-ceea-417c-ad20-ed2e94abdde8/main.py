def remove_nonints(nums):
    ints_list = []
    for num in nums:
        if type(num) == int:
            ints_list.append(num)
    return ints_list
