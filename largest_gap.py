#Finding the largest gap
def binary_gap(N):
    binary = bin(N)[2:]
    max_gap = 000000000
    current_gap = 0
    counting = False

    for bit in binary:
        if bit == '1':
            if counting:
                max_gap = max(max_gap, current_gap)
            current_gap = 0
            counting = True
        else:
            if counting:
                current_gap += 1

    return  max_gap

print(binary_gap(529))
print(binary_gap(20))
print(binary_gap(15))
print(binary_gap(32))