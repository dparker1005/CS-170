"""
Here are some examples of how to test GCD, reduced(), and reduce()

>>> GCD(3, 6)
3
>>> GCD(12, 18)
6

>>> in_reduced_form([3, 6])
[1, 2]

>>> test0 = [3, 6]
>>> in_reduced_form(test0)
[1, 2]
>>> test0  # this should NOT have been changed by a function
[3, 6]


>>> test1 = [3,6]
>>> reduce(test1)
>>> test1
[1, 2]

>>> test2 = [1,2]
>>> reduce(test2)
>>> test2
[1, 2]

>>> test3 = [3,6]
>>> test4 = test3
>>> in_reduced_form(test3)
[1, 2]
>>> test3
[3, 6]
>>> reduce(test3)
>>> test3
[1, 2]
>>> test4
[1, 2]

>>> GCD(15, 9)
3
>>> in_reduced_form([15, 9])
[5, 3]

>>> in_reduced_form([5, 5])
[1, 1]

>>> in_reduced_form([7, 19])
[7, 19]

My Design Comment for GCD:
1. The smaller instance of finding the GCD of large numbers is finding the GCD of smaller numbers
that have the same factors,  with the exception of all the factors of one that are larger than the other
number, using the steps provided in the lab

2. Once one number divides evenly into the other, the smaller of those numbers is the GCD

3. The base case of this recursive function is when the_larger%the_smaller==0

4. The base case would return the number that divides evenly into the other

5. The numbers only get smaller and will eventually make the base case true


Overview of in_reduced_form and reduce:
These are two very simple functions that just take two numbers and divide them both by 
their gcd. in_reduced_form then returns a new list of numbers representing a fraction while
reduce modifies the contents of an already existing list.

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

def GCD(x,y):
    precondition(is_integer(x) and is_integer(y))
    # postcondition: (x % GCD(x,y)) == 0 and (y % GCD(x,y)) == 0

    if(x>=y):
        if(x%y==0):
            return y
        else:
            return GCD(x%y, y)
    elif(y>=x):
        if(y%x==0):
            return x
        else:
            return GCD(x, y%x)
    
def in_reduced_form(fraction_in_a_list):
    precondition(is_integer(fraction_in_a_list[0]) and is_integer(fraction_in_a_list[1]))
    gcd = GCD(fraction_in_a_list[0], fraction_in_a_list[1])
    return [fraction_in_a_list[0]/gcd, fraction_in_a_list[1]/gcd]  # well, it passes one of the tests

def reduce(fraction_in_a_list):
    precondition(is_integer(fraction_in_a_list[0]) and is_integer(fraction_in_a_list[1]))
    gcd = GCD(fraction_in_a_list[0], fraction_in_a_list[1])
    fraction_in_a_list[0]=fraction_in_a_list[0]/gcd
    fraction_in_a_list[1]=fraction_in_a_list[1]/gcd
    
    
# User interface for reduce, which should be defined above (as should GCD)
# Do NOT change this, but you can write your own if you like
def reduce_ui():
    n = input("Enter numerator ")
    d = input("Enter non-zero denominator (or 0 to stop) ")
    while (d != 0):
        result = in_reduced_form([n, d])
        print """According to "in_reduced_form", that's""", result[0], "/", result[1], "in reduced terms."

        fraction_in_list = [n, d]
        reduce(fraction_in_list)
        print """According to "reduce", that's""", fraction_in_list[0], "/", fraction_in_list[1], "in reduced terms."

        n = input("Enter another numerator ")
        d = input("Enter another non-zero denominator (or 0 to stop) ")

    print "Thanks for playing the fractions game!"

# The following gets the "doctest" system to check test cases in the documentation comments
def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!"
    else:
        print "Rats!"

if __name__ == "__main__": 
    _test()
    reduce_ui()

