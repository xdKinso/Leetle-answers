# Write a function solve that finds the contiguous subarray with the largest sum in a list.
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4, 3, 4, -45, -5, 6, 3]
# expected output: 6

def solve(nums):
    #start max_sum with the first element of the list
    max_sum = nums[0]
    # start current_sum with the first element of the list
    current_sum = nums[0]
    # Iterate through the list starting from the second element since the first element is already looked at
    for i in range(1, len(nums)):
        # Update current_sum to be the maximum of the current element or the sum of current_sum and the current element
        current_sum = max(nums[i], current_sum + nums[i])
        # Update max_sum to be the maximum of max_sum and current_sum
        max_sum = max(max_sum, current_sum)
    # Return the maximum sum found
    return max_sum

# Print the result of the solve function with the given list
print(solve(nums))
# Time complexity: O(n)
# Space complexity: O(1)  # because we only use a constant amount of space to store the maximum sum and the current sum
