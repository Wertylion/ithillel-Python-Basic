# v1
nums = [1, 2, 3, 4, 5, 6]
#nums = [1, 2, 3]
#nums = [1, 2, 3, 4, 5]
#nums = [1]
#nums = []

middle = (len(nums)+1) // 2

nums1= nums[:middle]
nums2= nums[middle:]
result= [nums1, nums2]
print(result)


# v2

nums = [1, 2, 3, 4, 5, 6]
#nums = [1, 2, 3]
#nums = [1, 2, 3, 4, 5]
#nums = [1]
#nums = []
middle = len(nums) // 2

if len(nums) % 2 != 0:
    middle += 1

nums1 = nums[:middle]
nums2 = nums[middle:]
result = [nums1, nums2]
print(result)