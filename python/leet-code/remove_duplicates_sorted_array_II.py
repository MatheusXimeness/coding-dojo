# [0,0,1,1,1,1,2,3,3]

def remove_duplicates(nums):
    k = 1
    count = 1
    for idx in range(1, len(nums)):
        if nums[idx-1] == nums[idx]:
            count += 1
            if count == 2:
                nums[k] = nums[idx]
                k += 1
        else:
            nums[k] = nums[idx]
            count = 1
            k += 1

    return k

nums = [0,0,1,1,1,1,2,3,3]
remove_duplicates(nums)
print(nums)