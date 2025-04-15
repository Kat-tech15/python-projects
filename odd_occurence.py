def find_odd_occurrence(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

print(find_odd_occurrence([9,3,9,3,9,7,9]))
