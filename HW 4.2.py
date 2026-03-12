# [1, 3, 5] => 30
# [6] => 36
# [] => 0

nums = [1, 3, 5]

if len(nums) == 0:
    print(0)
else:
    print(sum(nums[::2]) * nums[-1])