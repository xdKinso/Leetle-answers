# Find an element in a list that only occurs once
# Time complexity O(n)
list = [3, 8, 3, 5, 3, 2, 7, 9, 8, 5, 3, 2, 7]

def singleElementDict(lst):
    counts = {}
    for num in lst:
        counts[num] = counts.get(num, 0) + 1
    for num, count in counts.items():
        if count == 1:
            return num
    return None

def singleElementXOR(lst):
    result = 0
    for num in lst:
        result ^= num
    return result

print("Using dictionary:", singleElementDict(list))
print("Using XOR:", singleElementXOR(list))