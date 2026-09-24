# i should remove the duplicates in place
# non-decreaseing order
# each unique element appears only once
# keep the order

# what is k -> a number of unique elements in nums -> is our returning
# the first k elements in nums should contain the unique numbers in sorted order. 

# [0,0,1,1,1,2,2,3,3,4] -> [0,4,1,1,1,2,2,3,3,4]
# index = 0 -> 1 -> 2
# last_pos = n-1
# curr_element = 0
# aux_count = 0
# unique element -> aux_count = 0 && curr_element = nums[index]
# not unique element -> change the curr_pos with the last -> zero to aux_count and increase pos

# [1,1,2]
def remove_duplicates(nums):
    k = 1
    for idx in range(1, len(nums)):
        if nums[idx] != nums[idx-1]:
            nums[k] = nums[idx]
            k += 1

    return k

nums = [0,0,1,1,1,2,2,3,3,4]
print(remove_duplicates(nums))
print(nums)