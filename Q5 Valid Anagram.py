#Write a function solve that determines if two strings are anagrams of each other. An anagram is a word formed by rearranging the letters of another word.
def solve(s1, s2):
    list1 = sorted(list(s1))
    list2 = sorted(list(s2))
    if list1 == list2:
        return True 
    else :
        return False
    
print(solve("anagram", "nagaram")) # True
# Time complexity: O(nlogn)
# Space complexity: O(n)
print(solve("rat", "car")) # False