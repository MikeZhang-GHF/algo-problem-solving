# def two_least_numbers(nums):
#     nums.sort()
#     return sum(nums[:2])

def two_least_numbers(nums):
    # a min, b second min
    a = b = float('inf')
    for x in nums:
        if x < a:
            b = a
            a = x
        elif x < b:
            b = x 
    return a + b 
            

nums = [8, 2, 9, 1, 7]
print(two_least_numbers(nums))