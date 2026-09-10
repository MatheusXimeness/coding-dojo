# You are given an array of integers nums and an integer target, return indices of the
# two numbers such that thet add up to target

# You may assume that each input would have exacly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Better Solution

def better_solution(nums, target):
    seen = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in seen:
            return [seen.get(diff), i]
        seen[nums[i]] = i
             

# Brute Force
def twoSum(nums, target):
        list = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                     continue
                else:
                    sum = nums[i] + nums[j]
                    if sum == target:
                        list.append(i)
                        list.append(j)
                        return list
                
nums = [3,3]
target = 6

print(twoSum(nums, target))
print(better_solution(nums, target))