The two object types use the functions in practically the same way. Usually,
one of the two types converts its data to the other type at the beginning
of each function to make the calculation easier. For minutes_until, they both
convert their data to minutes and simply subtract. For add minutes, 
Time_represented_by_seconds adds a ton of seconds by converting the minutes
while the other object type directly adds minutes and adjusts the rest of 
the data accordingly. For the __str__ function, Time_represented_by_seconds
converts its data to years, months, days, etc. Then it starts to build the return
string, determines if there is daylight savings time and finally completes
the string that will be returned. 