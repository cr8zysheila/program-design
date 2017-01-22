# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here
    if text == '':
        return (0, 0)

    subpalindrome = (palindrome_slice(text, i, j) 
        for i in range(0, len(text))
            for j in (i, i + 1))

    return max(subpalindrome, key = slice_len)
 
def slice_len(slice):
    return slice[1] - slice[0]

def palindrome_slice(text, L, R):
    "return (i, j) such that text[i:j] is the longest palindrome centered"
    "in index L and R. When testing odd palindrome, L == R"
    text = text.upper()
    start = L
    end = R

    while  L >= 0 and R <= len(text) - 1 and text[L] == text[R]:
        start = L
        end = R + 1
        L -= 1
        R += 1
    #print (start, end)
    return (start, end)


def test():
    L = longest_subpalindrome_slice
    #print L('racecar')
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()