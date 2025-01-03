# Find majority majorityElement in a list of integers. A majority element is an element that makes up more than half of the items in the list. If there is no majority element, the function should return None
# Solution 1
nums = [3, 2, 3, 3, 1, 2, 5, 6, 1, 3, 6, 8, 9, 2, 1, 2, 4, 6, 6, 6, 6, 6, 6, 6]
#0(nlogn) time complexity
def majorityElement(nums):
    nums.sort()
    candidate = nums[len(nums) // 2]
    count = nums.count(candidate)
    if count > len(nums) // 2:
        return candidate
    else:
        return None

result = majorityElement(nums)
if result is not None:
    print(result) 
# Solution 2    
#0(n) time complexity
def majorityElement2(nums):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    return max(counts, key=counts.get)

print(majorityElement2(nums))