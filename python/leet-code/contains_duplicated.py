def containsDuplicate(nums):
        duplicated = {}
        for i in range(len(nums)):
            if nums[i] in duplicated:
                return True
            duplicated[nums[i]] =+ 1
        return False

nums = [1,2,3,1]
print(containsDuplicate(nums))