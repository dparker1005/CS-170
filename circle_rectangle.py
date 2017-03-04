"""
    Test to see if a circular area and a rectangular area overlap.
    The circle is defined by a center x and y, and a radius 
        and the rectangle by xmin, xmax, ymin, ymax
    The parameters are those seven values, in the order above:
        center_x,center_y,radius,xmin,xmax,ymin,ymax
        
some examples:

# An obvious overlap:
>>> circle_rectangle_overlap(100,20,8, 80,120, 18,25)
True

# An obvious miss: Disproves #3,4,5
>>> circle_rectangle_overlap(100,20,8, 180,220, 18,25)
False

#Overlapping Pixels: Disproves #7
>>> circle_rectangle_overlap(1,1,0, 1,1, 1,1)
True

#Edge Cases:
#Top: Disproves #3,4,7
>>> circle_rectangle_overlap(3,1,1, 2,4, 2,4)
True

#Right: Disproves #4,5,7
>>> circle_rectangle_overlap(5,3,1, 2,4, 2,4)
True

#Bottom: Disproves #4,5,7
>>> circle_rectangle_overlap(3,5,1, 2,4, 2,4)
True

#Left: Disproves #3,4,7
>>> circle_rectangle_overlap(1,3,1, 2,4, 2,4)
True

#Corner Cases:
#North East: Disproves #4,5,7
>>> circle_rectangle_overlap(4,1,1, 2,4, 2,4)
True

#South East: Disproves #5,7
>>> circle_rectangle_overlap(4,5,1, 2,4, 2,4)
True

#South West: Disproves #3,5,7
>>> circle_rectangle_overlap(2,5,1, 2,4, 2,4)
True

#North West: Disproves #3,7
>>> circle_rectangle_overlap(2,1,1, 2,4, 2,4)
True

#Complete Box of Square: Disproves #3,6
>>> circle_rectangle_overlap( 352 ,  401 ,  109.01834708 ,  105 ,  243 ,  176 ,  317 )
False

"""

# make Python look in the right place for logic.py
import sys
sys.path.append('/home/courses/python')

from math import *
from logic import *
    

def circle_rectangle_overlap(center_x,center_y,radius,xmin,xmax,ymin,ymax):
    precondition(radius >= 0 and xmin <= xmax and ymin <= ymax)
    # postcondition: return true iff there exists x, y in both shapes...
    MODE='mine'  # set to 'test samples', 'answer key', 'code review', or 'mine'
    
    if MODE=='mine':
        if(point_in_rectangle(xmin, xmax, ymin, ymax, center_x, center_y+radius)):
           return True
        elif(point_in_rectangle(xmin, xmax, ymin, ymax, center_x, center_y-radius)):
           return True
        elif(point_in_rectangle(xmin, xmax, ymin, ymax, center_x-radius, center_y)):
           return True
        elif(point_in_rectangle(xmin, xmax, ymin, ymax, center_x+radius, center_y)):
           return True
        elif(point_in_circle(center_x, center_y, radius, xmin, ymin)):
            return True
        elif(point_in_circle(center_x, center_y, radius, xmin, ymax)):
            return True
        elif(point_in_circle(center_x, center_y, radius, xmax, ymin)):
            return True
        elif(point_in_circle(center_x, center_y, radius, xmax, ymax)):
            return True
        else:
            return False
    elif MODE=='code review':
        import circle_rectangle_to_review as review
        return review.circle_rectangle_overlap(center_x,center_y,radius,xmin,xmax,ymin,ymax)
    elif MODE=='answer key':
        print 'DAVE NEEDS TO FINISH THIS!'
    elif MODE=='test samples':
        from sample_answers.cs105.intersect.circle_rectangle_sample import circle_rectangle_overlap_samples
        answer = circle_rectangle_overlap_samples(center_x,center_y,radius,xmin,xmax,ymin,ymax)
        return answer
    else:
        print 'ERROR: You need to set MODE correctly in circle_rectangle_overlap in circle_rectangle.py'

def distance(x1,y1,x2,y2):
    return sqrt(pow((x1-x2),2)+pow((y1-y2),2))

def point_in_rectangle(xmin,xmax,ymin,ymax, x, y):
    if(xmin>x or xmax<x ):
        return False
    elif(ymin>y or ymax<y ):
        return False
    else:
        return True

def point_in_circle(center_x,center_y,radius, x, y):
    if(distance(center_x, center_y, x, y)<=radius):
        return True
    else:
        return False

# The following gets the "doctest" system to check test cases in the documentation comments
def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!"
    else:
        print "Rats!"

if __name__ == "__main__": _test()
