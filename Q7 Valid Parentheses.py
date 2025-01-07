#write a function  that determines if string "s"  of parentheses must be closed in the correct order/
# Example 1:
# Input: s = "()"
# Output: true
# Example 2:
# Input: s = "()[]{}"
# Output: true
# Example 3:
# Input: s = "(]"
# Output: false
#example 4:
# input : s = "(({{{))}]}}))"
def Valid_parentheses(s):
    stack = []
    # Create a dictionary to store the closing and opening parentheses
    mapping = {")": "(", "}": "{", "]": "["}
    # Iterate through the string
    for char in s:
        # If the character is an opening parenthesis, push it to the stack
        if char in mapping.values():
            stack.append(char)
        # If the character is a closing parenthesis
        elif char in mapping.keys():
            # If the stack is empty or the top of the stack does not match the current closing parenthesis
            if not stack or mapping[char] != stack.pop():
                return False
    # If the stack is empty, return True
    return not stack
# Test the function with the examples 
print(Valid_parentheses("()")) # True
print(Valid_parentheses("()[]{}")) # True
print(Valid_parentheses("(]")) # False
print(Valid_parentheses("(({{{))}]}}))")) # False
print(Valid_parentheses("(){()}[(])")) # True