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