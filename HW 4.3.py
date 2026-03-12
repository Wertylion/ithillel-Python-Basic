import random

nums = []
size = random.randint(3, 10)

for i in range(size):
    nums.append(random.randint(1, 9))

print(nums)

nums2 = [nums[0], nums[2], nums[-2]]
print(nums2)