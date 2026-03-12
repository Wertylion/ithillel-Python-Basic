# [0, 1, 0, 12, 3] -> [1, 12, 3, 0, 0]
# [0] -> [0]
# [1, 0, 13, 0, 0, 0, 5] -> [1, 13, 5, 0, 0, 0, 0]
# [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]

nums = [1, 0, 13, 0, 0, 0, 5]
n = nums.count(0)
for i in range(n):
    nums.remove(0)
    nums.append(0)
print(nums)






# nums.sort(key=lambda x: x == 0)
# print(nums)
