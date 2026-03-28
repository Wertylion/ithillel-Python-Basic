def difference (*nums):
    if not nums:
        return 0
    return round(max(nums) - min(nums),2)

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')

# nums = (10.2, -2.2, 0, 1.1, 0.5)
#
# if nums == ():
#     print("Empty list")
# else:
#     num = round(max(nums) - min(nums),2)
#     print(num)




# print(max(nums)min(nums))
