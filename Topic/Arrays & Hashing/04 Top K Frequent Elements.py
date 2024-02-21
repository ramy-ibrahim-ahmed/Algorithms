from collections import Counter


def topKFrequent(nums, k):
    frequent = Counter(nums)
    ordered_keys = list(key for key, value in frequent.most_common())[:k]
    return ordered_keys


# nums = [4, 1, -1, 2, -1, 2, 3]
# k = 2
# print(topKFrequent(nums, k))