# finding duplicates in arrays

def find_duplicates(nums):
    freq = {}
    duplicates = []
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] == 2:
            duplicates.append(num)

    return duplicates

print(find_duplicates([4,3,2,7,8,2,3,1]))

# reversing a given string in-place

def reverse_string(s):
    left, right = 0, len(s) -1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s
print(reverse_string(["h", "e", "l", "l", "o"]))


