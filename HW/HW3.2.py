nums1 = [12, 3, 4, 10]
if len(nums1) > 1:
    nums1.insert(0, nums1[-1])
    nums1.pop()

nums2 = [1]
if len(nums2) > 1:
    nums2.insert(0, nums2[-1])
    nums2.pop()

nums3 = []
if len(nums3) > 1:
    nums3.insert(0, nums3[-1])
    nums3.pop()

nums4 = [12, 3, 4, 10, 8]
if len(nums4) > 1:
    nums4.insert(0, nums4[-1])
    nums4.pop()


# [12, 3, 4, 10] => [10, 12, 3, 4]
# [1] => [1]
# [] => []
# [12, 3, 4, 10, 8] => [8, 12, 3, 4, 10]

print(nums1)
print(nums2)
print(nums3)
print(nums4)



