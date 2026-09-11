# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]

def remove_element(nums, val):
    last_pos = len(nums)
    i = 0
    while i < last_pos:
        if nums[i] == val:
            nums[i] = nums[last_pos - 1]
            last_pos -= 1
        else:
            i += 1

    return last_pos

nums = [0,1,2,2,2,0,4]
val = 2

print(remove_element(nums, val))
print(nums)