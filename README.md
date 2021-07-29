# Python-Essentials-LAB-3.4.1.13-Days-of-the-week

**Objectives**

•	improving the student's skills in defining classes from scratch;

•	defining and using instance variables;

•	defining and using methods.

**Scenario**

Your task is to implement a class called Weeker. Yes, your eyes don't deceive you - this name comes from the fact that objects of that class will be able to store and to manipulate days of a week.

The class constructor accepts one argument - a string. The string represents the name of the day of the week and the only acceptable values must come from the following set:
```
Mon Tue Wed Thu Fri Sat Sun
```
Invoking the constructor with an argument from outside this set should raise the WeekDayError exception. The class should provide the following facilities:

•	objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the same form as the constructor arguments;

•	the class should be equipped with one-parameter methods called add_days(n) and subtract_days(n), with n being an integer number and updating the day of week stored inside the object in the way reflecting the change of date by the indicated number of days, forward or backward.

•	all object's properties should be private;

**Expected output**
```
Mon
Thu
Sun
Sorry, I can't serve your request.
```

**Complete code includes**
```
class WeekDayError(Exception):
    pass

class Weeker:
    # This class is able to store and to manipulate days of a week
    # It uses dictionary to store names of the days

    def __init__(self, day):
        # This constructor initialises object with current day
        # and raises exception if day is not in "Mon Tue Wed Thu Fri Sat Sun"

    def __str__(self):
        # This method makes object printable

    def add_days(self, n):
        # This method adds n to the current day

    def subtract_days(self, n):
        # This method subtracts n from the current day
```
