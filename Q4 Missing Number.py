#write a function that finds the missing number in a list of numberrs from 0 to n, the list is missing one number
def missing_number(nums):
    s = sum(nums)
    s2 = sum([i+1 for i in range(len(nums))])
    if s == s2:
        return 0
    else:
        return s2 - s
    
print(missing_number([3,0,1])) # 2
print(missing_number([1,2,3])) # 0
print(missing_number([9,6,4,2,3,5,7,0,1])) # 8
# Time complexity: O(n)
# Space complexity: O(1)