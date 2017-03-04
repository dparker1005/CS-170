"""
#Test Suite

# A palindrome with an even number of letters:
>>> is_palindrome("sees")
True

# A palindrome with an odd number of letters:
>>> is_palindrome("racecar")
True

# A non-palindrome with an even number of letters:
>>> is_palindrome("mouse")
False

# A non-palindrome with an odd number of letters:
>>> is_palindrome("computer")
False

# A single letter (Assuming a single letter can be a palindrome):
>>> is_palindrome("a")
True


The goal of this program is to determine if a word is a palindrome, or if it 
reads the same forward and backwards. In order to solve this problem, I plan to use
basic recursive design. I will do this by comparing the first letter in the word to
the last letter in the word. If they are the same, I will run it through the algorithm
again after dropping the first and last letter. If they are not the same, the program
should return false because the word would not be a palindrome. The base case of this
program is if the length of the word is less than or equal to one. If this is the case,
the word is a palindrome and the function should return true.

"""

# make Python look in the right place for logic.py, or complain if it doesn't
try:
    import sys
    sys.path.append('/home/courses/python')
    from logic import *
except:
    print "Can't find logic.py; if this happens in the CS teaching lab, tell your instructor"
    print "   If you are using a different computer, add logic.py to your project"
    print "   (You can download logic.py from http://www.cs.haverford.edu/resources/software/logic.py)"
    sys.exit(1)

def is_palindrome(letters):

    if(len(letters)<=1): #Base case. If the input has one or less letters, the whole word is a palindrome. 
        return True
    elif(letters[0]==letters[len(letters)-1]): #Asks if the first letter is the same as the last letter
        return is_palindrome(letters[1:len(letters)-1]) #Calls this function again without the first and last letter
    else:
        return False #Returns false because the word cannot be a palindrome



# User interface for the palindrome function
def palindrome_ui():
    if __name__ == "__main__":
        print "Type 1 to run your test-suite, press 2 to type in your own tests:"
        answer = raw_input()
        if answer in ['1']:  
            _test()
        else:
            print "Please input a possible palindrome: "
            trial_text = raw_input()
            letters_only = lower_case_letters(trial_text)
            if is_palindrome(letters_only):
                print "The text '"+letters_only+"' is a palindrome"
            else:
                print "The text '"+letters_only+"' is not a palindrome."

"""
    make something all lower case letters, e.g.

>>> lower_case_letters('kayak')
'kayak'
>>> lower_case_letters('A man, a plan, a canal: Panama!')
'amanaplanacanalpanama'
"""

def lower_case_letters(text):
    if text == '':
        return ''
    else:
        first = text[0]
        rest  = text[1:len(text)]
        if first in 'abcdefghijklmnopqrstuvwxyz':  # already lower case
            return first + lower_case_letters(rest)
        elif first in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': # upper-case
            # lower(first) turns, for example, "D" into "d"
            from string import lower
            return lower(first) + lower_case_letters(rest)
        else:   # otherwise skip first element, as it's not a letter
            return lower_case_letters(rest)

# mostly copied from  http://docs.python.org/lib/module-doctest.html

def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!"
    else:
        print "Rats!"

# tests may or may not be chosen by the user interface...
if __name__ == "__main__": palindrome_ui()

