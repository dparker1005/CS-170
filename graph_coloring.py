"""
    CS105 second graph_coloring lab:
       finding all legal colorings of a Graph
       (start by finding _all_ colorings, and then integrate the testing function)
    
    Return a multi-line string made up of all legal colorings of a graph;
    collect_legal_colorings takes three parameters:
        states, a string of single-letter state names, e.g. "CMVHY"
                for Connecticut, Massachusetts, Vermont, new Hampshire, and new York
        colors, a string of single-letter color names, e,g. "rgb"
                for red, green, and blue
        borders, a string of pairs of letter of neighboring states, separated by spaces,
                e.g. 
                
    The result should have one coloring per line,
        with each line giving a space-separated set of pairs of state and color letters, e.g.
            Cr Mb Vr Hg Yg
            Cb Mr Vb Hg Yg
            ... etc
        for which the first line would tell us that Ct is red, Ma is blue, Vt is red, etc.
    
    The "return" (also known as "newline") characters in that string (e.g. after "Yg")
        can be entered into a Python program an "\n"
                
    NOTE that, for the graph coloring, it is fine to build an algorithm that ONLY
             works for the colors string "rgb" (we've put this is the precondition)
         HOWEVER, it must work for any set of single-letter state names and any
                  set of borders, even for "non-planar" graphs or graphs corresponding
                  to completely imaginary places!

    NOTE ALSO that the order of the reported colorings does not matter, so it is fine
        if your answer gives colorings in an order different from that shown below
        (in which case you should edit the doctest comments below accordingly).


EXAMPLES:

First, when there are no borders, any coloring is fine ...
  let's test this with something small, like Alaska and Hawaii

(Note that, for strings with newlines in them,
    we need to use "print" to show the newlines properly rather than as '\n';
    also DocTest expects "<BLANKLINE>" when printing a string ending with '\n')


# COMMENT OUT EITHER THIS OR THE ALTERNATIVE ABOVE.
# IN THIS VERSION, THE TEST DOES NOT EXPECT A SPACE " " AT THE END OF EACH LINE
# ALSO FEEL FREE TO REORDER AS NEEDED
>>> print collect_legal_colorings("AH", "rgb", "") # any order is fine here
Ar Hr
Ar Hg
Ar Hb
Ag Hr
Ag Hg
Ag Hb
Ab Hr
Ab Hg
Ab Hb
<BLANKLINE>

    
A more interesting example, with borders:
the five northeast states mentioned above can be colored in six ways
    (really, it's just the same pattern with red, green, and blue swapped around).


# COMMENT OUT EITHER THIS OR THE ALTERNATIVE ABOVE.
# IN THIS VERSION, THE TEST DOES NOT EXPECT A SPACE " " AT THE END OF EACH LINE
# ALSO FEEL FREE TO REORDER AS NEEDED
>>> print collect_legal_colorings("CMVHY", "rgb", "CM CY MV MH MY VH VY")  # Any order is fine here..
Cr Mg Vr Hb Yb
Cr Mb Vr Hg Yg
Cg Mr Vg Hb Yb
Cg Mb Vg Hr Yr
Cb Mr Vb Hg Yg
Cb Mg Vb Hr Yr
<BLANKLINE>


My Design Comment:
1. The smaller instance of finding all possible colorings of "ABCD" would 
be to find all possible colorings of "BCD" and appending it with each
possiblities for "A". Then you can find "CD" and append with all possibilties 
of "B"

2. Once all of the posibilities have been determined, you can get the 
complete solution by adding a "\n" to the end of every possibility and
appending all of the strings together.

3. Continuing recursion is necessary until states
has a length of 0. Therefore, the base case is when len(states)==0.

4. Non-Base Case would return:
get_all_colorings(states[1:],possible_combination+" "+states[0]+"r")+get_all_colorings(states[1:],possible_combination+" "+states[0]+"b")+get_all_colorings(states[1:],possible_combination+" "+states[0]+"g")

Base case would return: 
possible_combination+"\n"
In the future, this combination could also be tested here to see if it's valid using is_legal

5. If we keep on taking one character off of states, it will eventually reach 0 characters

SIDE NOTE: THIS SHOULD BE CALLED THROUGH ANOTHER FUNCTION THAT ONLY TAKES THE LIST OF STATES
AND MAKES SURE THAT A BLANK STRING IS PASSED FOR THE SECOND INPUT AND THAT ADDS
+<BLANKLINE> AT THE END OF THE STRING BEFORE RETURNING IT AND FUNCTION SHOULD HAVE PRECONDITION
THAT STATES CANNOT BE EMPTY

My Test Suite for get_all_colorings

#No Input, trips precondition
#>>> print start_get_all_colorings("", "")
#<BLANKLINE>

#Single Input
>>> print start_get_all_colorings("A", "")
Ar
Ag
Ab
<BLANKLINE>

#Multiple Inputs
>>> print start_get_all_colorings("AB", "")
Ar Br
Ar Bg
Ar Bb
Ag Br
Ag Bg
Ag Bb
Ab Br
Ab Bg
Ab Bb
<BLANKLINE>

#Multiple Inputs With Borders
>>> print start_get_all_colorings("ABCD", "AC AD BC BD CD")
Ar Br Cg Db
Ar Br Cb Dg
Ag Bg Cr Db
Ag Bg Cb Dr
Ab Bb Cr Dg
Ab Bb Cg Dr
<BLANKLINE>

#Everything connected to everything else
>>> print start_get_all_colorings("ABC", "AB BC AC")
Ar Bg Cb
Ar Bb Cg
Ag Br Cb
Ag Bb Cr
Ab Br Cg
Ab Bg Cr
<BLANKLINE>


is_valid test suite
#Everything is correct
>>> is_valid("Cr Mb Vr Hg Yg", "CM CY MV MH MY VH VY")
True

#Disproves #2
If Ct and Ma are both red, there's trouble
>>> is_valid("Cr Mr Vb Hg Yg", "CM CY MV MH MY VH VY")
False

#Disproves #2, 5
>>> is_valid('Qg Mr Or Gb Ag', 'QO QG MO MG MA OA GA')
False

#Disproves #2, 3, 6
>>> is_valid('Wg Zg Ob Hr Ab Br Cg', 'WO ZH OH AC CB BA CW')
False

#Disproves #2,5
>>> is_valid('Zr Wb Fb Rr Hr Mg Ig Jr', 'ZM WF WR WH WJ FR FH FM FI FJ RH RM RI RJ HM HI HJ MI MJ IJ')
False

#Disproves nothing
>>> is_valid('Ar Br Cr Dg Eb Fg Gb Hb', 'BH HA HF EA EC DH DG DB CF')
True

#2 Separate Countries
#Disproves #2, 3, 5
>>> is_valid('Ar Bb Cb Dg Er Fb', 'AC AB DF FE CB')
False

>>> is_valid('Cr Mg Vr Hb Yb', 'CM CY MV MH MY VH VY')
True


"""
# make Python look in the right place for logic.py
try:
    import sys
    sys.path.append('/home/courses/python')
    from logic import *
except:
    print "Can't find logic.py; if this happens in the CS teaching lab, tell your instructor"
    print "   If you are using a different computer, add logic.py to your project"
    print "   (You can download logic.py from http://www.cs.haverford.edu/resources/software/logic.py)"
    sys.exit(1)

# Now import the first half of the project:
from is_legal import is_a_legal_coloring, are_we_doing_doctest, we_are_doing_doctest, we_are_doing_coloring_enumeration
from string import *

def collect_legal_colorings(states, colors, borders):
    # Add a precondition, possibly including
    #    colors=="rgb"
    # to limit the case to 3-coloring of red, green, and blue
    # as well as anything else you can say about legal parameters
    
    # The next five lines ensure that, when doing graphics runs, we print out the parameters
    #  Please leave them alone, and write your answer below.
    we_are_doing_coloring_enumeration()
    want_to_print_stuff = not are_we_doing_doctest()
    if want_to_print_stuff:
        print "Calling collect_legal_colorings"
        print ">>> collect_legal_colorings('" + states + "', '" + colors + "', '" + borders + "')"

    MODE='mine'  # set to 'test samples', 'answer key', or 'mine'
    
    if MODE=='mine':
        answer = start_get_all_colorings(states, borders)  # REPLACE THIS WITH YOUR ALGORITHM.  Set the variable answer instead of doing a return if you want to see it printed automatically
    elif MODE=='test samples' or MODE=='answer key':
        try:
            """ Call all sample answers, see what answers we get ... """
            from sample_answers.cs105.graph_coloring.enumeration_samples import collect_legal_colorings_samples_all
            from sample_answers.cs105.graph_coloring.enumeration_samples import collect_legal_colorings_samples_correct
            # set the following to only use the correct one!
            enumeration_samples_just_do_the_right_ones = (MODE=='answer key')
        
            if enumeration_samples_just_do_the_right_ones:
                answer = collect_legal_colorings_samples_correct(states, colors, borders)
            else:
                answer = collect_legal_colorings_samples_all(states, colors, borders)
        except:
            print "Hmmmm... can't find sample answers. This shouldn't happen on the CS teaching lab computers"
            print " If you are running this program on another computer, you'll have to wait to check"
            print " your test suite against the sample answers when you're back in the lab."
            print " (Remember to Team->Commit on your computer and Team->Update in the lab.)"
            answer = ""
    else:
        answer = 'ERROR: You need to set MODE correctly in graph_coloring.py'

    # Leave the next line alone, too, to ensure proper printing in the GUI
    we_are_doing_coloring_enumeration(False) # done with this enumeration

    if want_to_print_stuff:
        print answer
    return answer

#My Functions
def start_get_all_colorings(states, borders):
    precondition(is_string(states) and states!="")
    return get_all_colorings(states, "", borders)

def get_all_colorings(states, possible_combination, borders):
    precondition(is_string(states) and is_string(possible_combination))
    if(len(states)==0):
        if(is_valid(possible_combination[1:], borders)):
            return possible_combination[1:]+"\n" #there will always be a space in front, need to delete
        else:
            return ""
    else:
        return (get_all_colorings(states[1:],possible_combination+" "+states[0]+"r", borders)+
                get_all_colorings(states[1:],possible_combination+" "+states[0]+"g", borders)+
                get_all_colorings(states[1:],possible_combination+" "+states[0]+"b", borders))

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

# The next two functions are used to make the test suite less dependent on ordering.
# The first uses some fancy Python stuff from "from string import *";
#    the second basic recursive design and functions-in-functions
# CS105 students should NOT worry about understanding _how_ they work!

# how many solutions are in a set of colorings (just counts the number of \n's)
def count_solutions(set_of_colorings):
    precondition(True)  # Always does *something*, but complains in a useful way about bad parameters
    
    if set_of_colorings == None:
        return ("Error: count_solutions called with None as a parameter.\n"+
                "       This typically means the function that produced its parameter lacks a return in some case")
    elif not isinstance(set_of_colorings, basestring):
        return ("Error: count_solutions called with a non-string parameter.\n"+
                "       This typically means the function that produced its parameter returned something else")

    else:
        return set_of_colorings.count("\n")

# true or false --- does set_of_colorings have the coloring?
def has_this_coloring(set_of_colorings, this_coloring):
    precondition(True)  # Always does *something*, but complains in a useful way about bad parameters
    
    if set_of_colorings == None:
        return ("Error: count_solutions called with None as a set_of_colorings parameter.\n"+
                "       This typically means the function that produced its first parameter lacks a return in some case")
    elif not isinstance(set_of_colorings, basestring):
        return ("Error: count_solutions called with a non-string as a set_of_colorings parameter.\n"+
                "       This typically means the function that produced its first parameter returned something else")
    elif not isinstance(this_coloring, basestring):
        return ("Error: count_solutions called with a non-string as a this_coloring parameter.\n"+
                "       Make sure the second parameter is a string")
    elif "\n" in this_coloring:
        return ("Error: count_solutions called with a multi-line string as a this_coloring parameter.\n"+
                "       Make sure the second parameter just a single coloring")

    else:

        def list_has_coloring(list_of_colorings, this_one):
            def same_coloring(c1, c2):
                def subset_coloring(c1, c2):  # are all state/color pairs in c1 also in c2?
                    if (len(c1) < 2):
                        return True
                    else:
                        return c1[0:2] in c2 and subset_coloring(c1[3:], c2)
                return subset_coloring(c1, c2) and subset_coloring(c2, c1)
            if len(list_of_colorings) == 0:
                return False
            else:
                return (same_coloring(list_of_colorings[0], this_one) or
                        list_has_coloring(list_of_colorings[1:], this_one))
        return list_has_coloring(set_of_colorings.split("\n"), this_coloring)


# The following gets the "doctest" system to check test cases in the documentation comments
def _test():
    we_are_doing_doctest()  # prevent is_legal from printing debugging info
    import doctest
    return doctest.testmod()

if __name__ == "__main__":
    print "Running 'doctest' tests for graph coloring enumeration. These may take a little time..."
    print " To use the graphical interface, run A_graphical_user_interface.py"
    result = _test()
    if result[0] == 0:
        print "Congratulations! You have passed all" , result[1], "coloring enumeration tests"
    else:
        print "Rats!"
