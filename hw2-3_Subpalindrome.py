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

    even_subpalindrome = (palindrome_slice(text, i, True) for i in 
        range(0, len(text)))

    odd_subpalindrome = (palindrome_slice(text, i, False) for i in 
        range(0, len(text)))

    longest_even = max(even_subpalindrome, key = slice_len)
    longest_odd = max(odd_subpalindrome, key = slice_len)
    return max(longest_even, longest_odd, key = slice_len)
 
def slice_len(slice):
    return slice[1] - slice[0]

def palindrome_slice(text, m, even=False):
    "return (i, j) such that text[i:j] is the longest palindrome centered"
    "in index m, if even==false. If even is true, then the center is m and m+1"
    text = text.upper()
    start = m
    end = m + 1

    ''' this border case exams are not necessary
    if (m == 0 and not even) or (m == len(text) - 1)
        return (start, end)
    '''

    j = m+1
    if even:
        i = m
    if not even:
        i = m - 1

    while  i >= 0 and j <= len(text) - 1 and text[i] == text[j]:
        start = i
        end = j + 1
        i -= 1
        j += 1
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