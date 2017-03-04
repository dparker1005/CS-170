"""
   A python class to represent time on the planet Regulus,
       as described in the lab assignment.

Examples:

>>> t1 = Time(03 + 60 * (25 + 60 * (01 + 24 * ((01-1) + 30 * ((04-1) + 12 * (12-1))))))
>>> print t1	# 04/01/12 01:25:03 AM RST     (or, if you like, 12-04-01 1:15:03 RST)
4/01/12 1:25:03 AM RST

>>> t1_original = deepcopy(t1)
>>> t1.add_minutes(-120)
>>> print t1					# 120 minutes before 04/01/12 01:25:03 AM RST
3/30/12 11:25:03 PM RST
>>> t1 = deepcopy(t1_original)

>>> t1.add_minutes(-60)
>>> print t1					#  60 minutes before 04/01/12 01:25:03 AM RST
4/01/12 12:25:03 AM RST
>>> t1 = deepcopy(t1_original)

>>> t1.add_minutes(60)
>>> print t1					#  60 minutes after  04/01/12 01:25:03 AM RST, i.e. into DST
4/01/12 3:25:03 AM RDT
>>> t1 = deepcopy(t1_original)


>>> Time(344775540).minutes_until(Time(344775900))  # from the assignment
6

# t2 is "10/01/12 01:55:57 AM RDT"
#  that's a total of 57 seconds plus 60*55 seconds ... minus 1 hour
>>> t2 = Time(57 + 60 * (55 + 60 * (01 + 24 * ((01-1) + 30 * ((10-1) + 12 * (12-1))))) - 3600)
>>> print t2  # "1:55:57 AM on October 1, year 12 prints as: "
10/01/12 1:55:57 AM RDT

>>> print t1.minutes_until(t2)	# 10/01/12 01:55:57 AM RDT   vs.   04/01/12 01:25:03 AM RST
259170
>>> print t2.minutes_until(t1)	# 04/01/12 01:25:03 AM RST   vs.   10/01/12 01:55:57 AM RDT  # note -259171 is fine too
-259170

>>> t2.add_minutes(60)
>>> print t2	# 1 hour  after "1:55:57 AM on October 1, year 12"
10/01/12 2:55:57 AM RDT
>>> t2.add_minutes(60)
>>> print t2	# 2 hours after "1:55:57 AM on October 1, year 12"
10/01/12 2:55:57 AM RST
>>> t2.add_minutes(60)
>>> print t2	# 3 hours after "1:55:57 AM on October 1, year 12"
10/01/12 3:55:57 AM RST

>>> t3 = deepcopy(t1)
>>> t3.add_minutes(  3)
>>> t1.minutes_until(t3)
3
>>> t3 = deepcopy(t1)
>>> t3.add_minutes(-60)
>>> t1.minutes_until(t3)
-60
>>> t3 = deepcopy(t1)
>>> t3.add_minutes(-60)
>>> t3.minutes_until(t1)
60
>>> t3 = deepcopy(t1)
>>> t3.add_minutes(  0)
>>> t1.minutes_until(t3)
0
>>> t3 = deepcopy(t1)
>>> t3.add_minutes( 60)
>>> t1.minutes_until(t3)
60
>>> t3 = deepcopy(t1)
>>> t3.add_minutes(120)
>>> t1.minutes_until(t3)
120
>>> t3 = deepcopy(t1)
>>> t3.add_minutes(180)
>>> t1.minutes_until(t3)
180

>>> t3 = deepcopy(t2)
>>> t3.add_minutes(  3)
>>> t2.minutes_until(t3)
3
>>> t3 = deepcopy(t2)
>>> t3.add_minutes(-60)
>>> t2.minutes_until(t3)
-60
>>> t3 = deepcopy(t2)
>>> t3.add_minutes(  0)
>>> t2.minutes_until(t3)
0
>>> t3 = deepcopy(t2)
>>> t3.add_minutes( 60)
>>> t2.minutes_until(t3)
60
>>> t3 = deepcopy(t2)
>>> t3.add_minutes(120)
>>> t2.minutes_until(t3)
120
>>> t3 = deepcopy(t2)
>>> t3.add_minutes(180)
>>> t2.minutes_until(t3)
180

>>> tx = Time(121)
>>> ty = Time(59)
>>> ty.minutes_until(tx)
1

"""
from copy import deepcopy
from pandas.core.common import is_integer
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


class Time_represented_by_seconds:
    def __init__(self, seconds):
        precondition(is_integer(seconds) and seconds>=0)
        self.seconds = seconds   
    def minutes_until(self, time):
        #precondition(time is a Time_represented_by_seconds)
        return time.seconds//60-self.seconds//60    
    def add_minutes(self, minutes_to_add):
        precondition(is_integer(minutes_to_add))
        self.seconds = self.seconds+(minutes_to_add*60)
    def __str__(self):
        temp_seconds = self.seconds
        years = temp_seconds//31104000
        temp_seconds = temp_seconds%31104000
        months = temp_seconds//2592000
        temp_seconds = temp_seconds%2592000
        days = temp_seconds//86400
        temp_seconds = temp_seconds%86400
        hours = temp_seconds//3600
        temp_seconds = temp_seconds%3600
        minutes = temp_seconds//60
        seconds = temp_seconds%60 
        
        to_return = ""
        to_return+=str(months+1)
        to_return+="/"
        if(days<10):
            to_return+="0"
        to_return+=str(days+1)
        to_return+="/"
        to_return+=str(years%100+1)
        to_return+=" "
        
        
        daylight_savings_addition = 0 #will be 0 if no daylight savings, 1 if there is
        if(3<months<9):
            daylight_savings_addition = 1
        elif(months == 3 and days>0):
            daylight_savings_addition = 1
        elif(months == 3 and hours>1):
            daylight_savings_addition = 1
        elif(months == 9 and days==0 and hours<2):
            daylight_savings_addition = 1
        
        temp_hours = hours+daylight_savings_addition
        if(hours>12):
            temp_hours-=12
        elif(hours==0 and daylight_savings_addition==0):
            temp_hours= 12
        elif(hours==0 and daylight_savings_addition==1):
            temp_hours= 1
        to_return+=str(temp_hours)
        to_return+=":"
        if(minutes<10):
            to_return+="0"
        to_return+=str(minutes)
        to_return+=":"
        if(seconds<10):
            to_return+="0"
        to_return+=str(seconds)
        to_return+=" "
        if(hours>12):
            to_return+="PM "
        else:
            to_return+="AM "
        if(daylight_savings_addition==0):
            to_return+="RST"
        else:
            to_return+="RDT"
        return to_return

class Time_represented_by_clock_and_calendar:
    def __init__(self, seconds):
        precondition(is_integer(seconds) and seconds>=0)
        self.years = seconds//31104000
        seconds = seconds%31104000
        self.months = seconds//2592000
        seconds = seconds%2592000
        self.days = seconds//86400
        seconds = seconds%86400
        self.hours = seconds//3600
        seconds = seconds%3600
        self.minutes = seconds//60
        self.seconds = seconds%60       
    def minutes_until(self, time):
        #precondition(time is a Time_represented_by_clock_and_calendar)
        return (time.years*518400+time.months*43200+time.days*1440+time.hours*60+time.minutes)-(self.years*518400+self.months*43200+self.days*1440+self.hours*60+self.minutes)  
    def add_minutes(self, minutes_to_add):
        precondition(is_integer(minutes_to_add))
        self.minutes = self.minutes+minutes_to_add
        self.hours = self.hours+self.minutes//60
        self.days = self.days+self.hours//24
        self.months = self.months+self.days//30
        self.years = self.years+self.months//12        
        self.minutes = self.minutes%60
        self.hours = self.hours%24
        self.days = self.days%30
        self.months = self.months%12
    def __str__(self):
        to_return = ""
        to_return+=str(self.months+1)
        to_return+="/"
        if(self.days<10):
            to_return+="0"
        to_return+=str(self.days+1)
        to_return+="/"
        to_return+=str(self.years%100+1)
        to_return+=" "
        
        
        daylight_savings_addition = 0 #will be 0 if no daylight savings, 1 if there is
        if(3<self.months<9):
            daylight_savings_addition = 1
        elif(self.months == 3 and self.days>0):
            daylight_savings_addition = 1
        elif(self.months == 3 and self.hours>1):
            daylight_savings_addition = 1
        elif(self.months == 9 and self.days==0 and self.hours<2):
            daylight_savings_addition = 1
        
        temp_hours = self.hours+daylight_savings_addition
        if(self.hours>12):
            temp_hours-=12
        elif(self.hours==0 and daylight_savings_addition==0):
            temp_hours= 12
        elif(self.hours==0 and daylight_savings_addition==1):
            temp_hours= 1
        to_return+=str(temp_hours)
        to_return+=":"
        if(self.minutes<10):
            to_return+="0"
        to_return+=str(self.minutes)
        to_return+=":"
        if(self.seconds<10):
            to_return+="0"
        to_return+=str(self.seconds)
        to_return+=" "
        if(self.hours>12):
            to_return+="PM "
        else:
            to_return+="AM "
        if(daylight_savings_addition==0):
            to_return+="RST"
        else:
            to_return+="RDT"
        return to_return
# by default, use the first representation, but this is changed in DocTest below
Time = Time_represented_by_seconds

# mostly copied from  http://docs.python.org/lib/module-doctest.html
def _test():
    import doctest
    global Time
    Time = Time_represented_by_seconds
    result = doctest.testmod()
    print "Result of doctest for Time_represented_by_seconds is:",
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], "tests!"
    else:
        print "Rats!"

    print "\n\n\n\n"
    
    Time = Time_represented_by_clock_and_calendar
    result = doctest.testmod()
    print "Result of doctest for Time_represented_by_clock_and_calendar is:",
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], "tests!"
    else:
        print "Rats!"
    Time = Time_represented_by_seconds

if __name__ == "__main__":
    _test()
