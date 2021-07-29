# This is the Python Essentials 2 LAB 3.4.1.13 Days of the week
# V2 stores names of the days in tuple. It works faster

class WeekDayError(Exception):
    pass
	

class Weeker:
    # This class is able to store and to manipulate days of a week
    # It uses tuple to store names of the days
    __days_week = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

    def __init__(self, day):
        # This constructor initializes object with current day
        # and raises exception if day is not in "Mon Tue Wed Thu Fri Sat Sun"
        if day in Weeker.__days_week:
            self.__day = Weeker.__days_week.index(day)
        else:
            raise WeekDayError

    def __str__(self):
        # This method makes object printable
        return Weeker.__days_week[self.__day]

    def add_days(self, n):
        # This method adds n to the current day and skips whole weeks 
        self.__day += n % 7

    def subtract_days(self, n):
        # This method subtracts n from the current day and skips whole weeks 
        self.__day -= n % 7 


if __name__ == "__main__":
    # This code implements some test cases
    # Expected output:
    # Mon
    # Tue
    # Sun
    # Sorry, I can't serve your request.
    try:
        weekday = Weeker('Mon')
        print(weekday)
        weekday.add_days(15)
        print(weekday)
        weekday.subtract_days(23)
        print(weekday)
        weekday = Weeker('Monday')
    except WeekDayError:
        print("Sorry, I can't serve your request.")

