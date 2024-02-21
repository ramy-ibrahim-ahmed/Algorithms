from functools import reduce


def productExceptSelf(nums):
    result = []
    for i in range(len(nums)):
        n = nums[:]
        del n[i]
        result.append(reduce(lambda x, y: x * y, n))
    return result


def productExceptSelf(nums):
    res = [None] * len(nums)
    product = 1
    for i in range(len(nums)):
        res[i] = product
        product *= nums[i]
    product = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= product
        product *= nums[i]
    return res


# nums1 = [1, 2, 3, 4]
# print(productExceptSelf(nums1))

# nums2 = [-1, 1, 0, -3, 3]
# print(productExceptSelf(nums2))