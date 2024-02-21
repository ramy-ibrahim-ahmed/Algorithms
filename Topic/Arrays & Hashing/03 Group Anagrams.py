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