To use Time_represented_by_seconds and Time_represented_by_clock_and_calendar,
you just need to call either of them with the total seconds since
January 1, 1970. This input must be a positive integer value. 

Regardless of which of the above objects you use to use, you will have
access to two methods: minutes_until and add_minutes. minutes_until will compare
two time objects OF THE SAME TYPE and tell you the difference in the time.
add_minutes allows you to add an integer value of minutes to the given object.

Both Time_represented_by_seconds and Time_represented_by_clock_and_calendar work
exactly the same way and are indistinguishable without looking at the code. 
They both also have a formatted print function to make their outputs readable.