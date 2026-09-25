from collections import Counter
# [2,2,1,1,1,2,2]
# [2,2,1,1,1,1,1,2,2]

def majority_element_with_more_space(nums):
    majority_limit = len(nums) // 2
    counts = Counter(nums)
    result = 0

    for key, value in counts.items():
        if value > majority_limit:
            majority_limit = value
            result = keyw
    return result

def majority_element_better_solution(nums):
    count = 0
    candidate = 0 
    for num in nums:
        if num != candidate:
            if count == 0:
                candidate = num
                count = 1
            else:
                count -= 1
        else:
            count += 1

    return candidate


nums = [2,2,1,1,1,1,1,2,2]
print(majority_element_better_solution(nums))