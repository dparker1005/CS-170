"""
    CS105 first graph_coloring lab:
     determining whether or not a proposed coloring for a graph is legal
    
    is_a_legal_coloring should return True if the coloring is legal, and False otherwise
    
    it takes two parameters,
        possible_coloring, a proposed coloring
            Each state will be represented by a single letter such as V for Vermont,
                and each color with a single letter such as r for red, and thus the
                coloring will be a space-separated set of pairs of state and color letters,
                e.g. "Cr Mb Vr Hg Yg" could mean Ct is red, Ma is blue, Vt is red, etc.
        borders, a set of borders, e.g. "CM CY MV MH MY VH VY" for Ct bordering Ma, etc.
        
Examples:

#Everything is correct
>>> is_a_legal_coloring("Cr Mb Vr Hg Yg", "CM CY MV MH MY VH VY")
True

#Disproves #2
If Ct and Ma are both red, there's trouble
>>> is_a_legal_coloring("Cr Mr Vb Hg Yg", "CM CY MV MH MY VH VY")
False

#Disproves #2, 5
>>> is_a_legal_coloring('Qg Mr Or Gb Ag', 'QO QG MO MG MA OA GA')
False

#Disproves #2, 3, 6
>>> is_a_legal_coloring('Wg Zg Ob Hr Ab Br Cg', 'WO ZH OH AC CB BA CW')
False

#Disproves #2,5
>>> is_a_legal_coloring('Zr Wb Fb Rr Hr Mg Ig Jr', 'ZM WF WR WH WJ FR FH FM FI FJ RH RM RI RJ HM HI HJ MI MJ IJ')
False

#Disproves nothing
>>> is_a_legal_coloring('Ar Br Cr Dg Eb Fg Gb Hb', 'BH HA HF EA EC DH DG DB CF')
True

#2 Separate Countries
#Disproves #2, 3, 5
>>> is_a_legal_coloring('Ar Bb Cb Dg Er Fb', 'AC AB DF FE CB')
False

The goal of this function is to determine if adjacent states have the same coloring.
I plan to do this by using two sets of recursive designs. The first design will
take the coloring that we want to determine if it is valid and the connections 
between the states. The fist base case is if there are no borders in the list
which, as you will see, will actually never trigger unless the user passes in
a blank string for borders. After determining that there are indeed borders, 
the function will then get the first and second state by asking for the first
and second characters of the borders string. After getting the states, the function
then gets the color of each of the states via another function, color_of, which will
be described later. After getting the colors, the function asks if the colors are not the same. 
If they are indeed the same, the function should return false because that means that two
adjacent states have the same color. If they are not the same, the function asks if there are
only two characters left in the borders string, which is a base case. If this is true, then the coloring of the whole
map is valid. If not, the method calls itself after removing the first 3 characters
(state1, state2, and the space) and checks the next set of borders. 

The color_of function takes in the possible coloring that is being tested as well as the state
that is being asked about. It is also a recursive function. The base case, which should never 
happen unless there is user error, is if possible coloring has 0 characters in it, which then 
returns a blank string. Assuming this isn't the case,the function asks if the first character
is the state being tested for. If it is, the function will return the second character,
which would be the color of the state. If the state does not match the first character,
the function will ask if there are less than 2 characters left. If this is true, it will return
a blank string for the same reason as the base case. If there are more than 2 characters,
the function will call itself again after cutting the first 3 characters of possible_colloring
(the state, the color and a space). When paired, these two functions are able to determine
if a possible coloring of states have any adjacent colors that are the same.

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

def is_a_legal_coloring(possible_coloring, borders):
    # Fill in a precondition here


    # The next two lines will ensure that, when doing graphics for coloring testing,
    #   we print out the parameters (without printing them when running doctest).
    # We also don't print the questions when testing the enumeration function
    #   (unlesss of course the "and not doing_coloring_enumeration" gets commented out...)
    want_to_print_stuff = not are_we_doing_doctest() and not are_we_doing_coloring_enumeration()
    if want_to_print_stuff:
        print "Calling is_a_legal_coloring..."
        print ">>> is_a_legal_coloring('"+ possible_coloring + "', '" + borders + "')"

    MODE='mine'  # set to 'test samples', 'answer key', or 'mine'
    
    if MODE=='mine':
        #call recursive method that goes through borders one at a time and checks if each one is valid
        answer = is_valid(possible_coloring, borders);
        
    elif MODE=='test samples' or MODE=='answer key':
        try:
            from sample_answers.cs105.graph_coloring.testing_samples import is_a_legal_coloring_samples_correct, is_a_legal_coloring_samples_all
        
            # set the following to only use the correct one!
            coloring_testing_samples_just_do_the_right_ones = (MODE=='answer key' or are_we_doing_coloring_enumeration())
        
            if coloring_testing_samples_just_do_the_right_ones:
                answer = is_a_legal_coloring_samples_correct(possible_coloring, borders)
            else:
                answer = is_a_legal_coloring_samples_all(possible_coloring, borders)
            
        except:
            print "Hmmmm... can't find sample answers. This shouldn't happen on the CS teaching lab computers"
            print " If you are running this program on another computer, you'll have to wait to check"
            print " your test suite against the sample answers when you're back in the lab."
            print " (Remember to Team->Commit on your computer and Team->Update in the lab.)"
    
            answer= False  # Well, sometimes this is the right answer!
    else:
        answer = 'ERROR: You need to set MODE correctly in is_legal.py'


    if want_to_print_stuff:
        print answer
    return answer  

#my functions:
def is_valid(possible_coloring, borders):
    if(len(borders)==0): #should never happen unless user passes blank string for borders
        return True;
    else:
        state1 = borders[0]; #get the first 2 states from borders
        state2 = borders[1];
        color1 = color_of(possible_coloring, state1); #get the colors for the states
        color2 = color_of(possible_coloring, state2);
        if(color1!=color2): #asks if colors are different
            if(len(borders)==2): #if these are the last 2 states to be compared
                return True;
            else:
                return is_valid(possible_coloring, borders[3:len(borders)]); #chops off first 3 characters
        else:
            return False; #returns false if adjacent states have same color
        
        
def color_of(possible_coloring, state):
    if(len(possible_coloring)==0): #should never happen unless user passes blank string for possible_coloring
        return "";
    elif(possible_coloring[0]==state): #checks if first character of possible_coloring is the state to be tested
        return possible_coloring[1]; #returns the color of the state
    else:
        if(len(possible_coloring)<=2): #in case there are no more states to test
            return "";
        else:
            return color_of(possible_coloring[3:len(possible_coloring)], state); #chops first 3 characters
           


#
# The stuff below makes sure the two files can communicate about things
#  like whether or not we're doing doctest,
#  to control whether things are printed
#
doing_doctest_for_graph_coloring = False  # This is automatically reset to True when we do doctest tests; it controls printing
doing_coloring_enum              = False  # This is automatically reset to True for Lab 3 but not Lab 4

INSANE_DEBUGGING = False  # can't get the debugger to play nice with doctest, AND I'm trying to debug doctest :-(
def are_we_doing_doctest():  # I can import a function but not a variable into Lab 4
    global doing_doctest_for_graph_coloring
    if INSANE_DEBUGGING:
        print("In are_we_doing_doctest? returning " + str(doing_doctest_for_graph_coloring))
    return doing_doctest_for_graph_coloring

def we_are_doing_doctest(well_are_we = True):
    global doing_doctest_for_graph_coloring
    if INSANE_DEBUGGING:
        print("in we_are_doing_doctest, setting to " + str(well_are_we))
    doing_doctest_for_graph_coloring = well_are_we

def are_we_doing_coloring_enumeration():  # I can import a function but not a variable into Lab 4
    global doing_coloring_enum
    return doing_coloring_enum

def we_are_doing_coloring_enumeration(well_are_we = True):
    global doing_coloring_enum
    doing_coloring_enum = well_are_we


# The following gets the "doctest" system to check test cases in the documentation comments
# see  http://docs.python.org/lib/module-doctest.html
def _test_is_legal():
    print "Running 'doctest' tests for graph coloring testing function."
    print " To use the graphical interface, run A_graphical_user_interface.py"
    we_are_doing_doctest()
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!"
    else:
        print "Rats!"

if __name__ == "__main__": _test_is_legal()
