################################################################################## 217. Contains Duplicate #
def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# nums = [1, 2, 3, 1]
# print(containsDuplicate(nums))

# nums = [1, 2, 3, 4]
# print(containsDuplicate(nums))

# nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# print(containsDuplicate(nums))


####################################################################################### 242. Valid Anagram #
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    a = sorted(s)
    b = sorted(t)
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


# s = "anagram"
# t = "nagaram"
# print(isAnagram(s, t))

# s = "rat"
# t = "car"
# print(isAnagram(s, t))


############################################################################################### 1. Two Sum #
def twoSum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return None


# nums = [2, 7, 11, 15]
# target = 9
# print(twoSum(nums, target))

# nums = [3, 2, 4]
# target = 6
# print(twoSum(nums, target))

# nums = [3, 3]
# target = 6
# print(twoSum(nums, target))

# nums = [3, 2, 3]
# target = 6
# print(twoSum(nums, target))


####################################################################################### 49. Group Anagrams #
def groupAnagrams(strs):
    str_dict = {}
    for word in strs:
        sorted_word = "".join(sorted(word))
        str_dict.setdefault(sorted_word, []).append(word)
    return list(str_dict.values())


# strs = ["eat","tea","tan","ate","nat","bat"]
# print(groupAnagrams(strs))

# strs = [""]
# print(groupAnagrams(strs))

# strs = ["a"]
# print(groupAnagrams(strs))

############################################################################# 347. Top K Frequent Elements #
from collections import Counter


def topKFrequent(nums, k):
    frequent = Counter(nums)
    ordered_keys = list(key for key, value in frequent.most_common())[:k]
    return ordered_keys


# nums = [4, 1, -1, 2, -1, 2, 3]
# k = 2
# print(topKFrequent(nums, k))


######################################################################## 238. Product of Array Except Self #
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


######################################################################################### 36. Valid Sudoku #
from collections import defaultdict


def isValidSudoku(board):
    for i in range(9):
        row_seen = set()
        col_seen = set()
        square_seen = set()

        for j in range(9):
            # Check rows
            if board[i][j] != ".":
                if board[i][j] in row_seen:
                    return False
                row_seen.add(board[i][j])

            # Check columns
            if board[j][i] != ".":
                if board[j][i] in col_seen:
                    return False
                col_seen.add(board[j][i])

            # Check squares
            square_row = 3 * (i // 3)
            square_col = 3 * (i % 3)
            if board[square_row + j // 3][square_col + j % 3] != ".":
                if board[square_row + j // 3][square_col + j % 3] in square_seen:
                    return False
                square_seen.add(board[square_row + j // 3][square_col + j % 3])
    return True


def isValidSudoku(board):
    rows = defaultdict(set)
    col = defaultdict(set)
    square = defaultdict(set)
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                continue
            else:
                if (
                    board[i][j] in rows[i]
                    or board[i][j] in col[j]
                    or board[i][j] in square[(3 * (i // 3) + j // 3)]
                ):
                    return False
                rows[i].add(board[i][j])
                col[j].add(board[i][j])
                square[(3 * (i // 3) + j // 3)].add(board[i][j])
    return True


# board = [
#     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
#     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#     [".", "9", "8", ".", ".", ".", ".", "6", "."],
#     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#     [".", "6", ".", ".", ".", ".", "2", "8", "."],
#     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#     [".", ".", ".", ".", "8", ".", ".", "7", "9"],
# ]
# print(isValidSudoku(board))

# board = [
#     ["8", "3", ".", ".", "7", ".", ".", ".", "."],
#     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#     [".", "9", "8", ".", ".", ".", ".", "6", "."],
#     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#     [".", "6", ".", ".", ".", ".", "2", "8", "."],
#     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#     [".", ".", ".", ".", "8", ".", ".", "7", "9"],
# ]
# print(isValidSudoku(board))