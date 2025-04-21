#non-repeating character
from collections import Counter

def first_non_repeating_char(s):
    freq = Counter(s)
    for char in s:
        if freq[char] == 1:
            return char
    return -1

print(first_non_repeating_char("aabbcde"))

#
def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

print(two_sum([2,7,11,15], 9))
