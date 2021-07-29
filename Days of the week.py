# This is the Python Essentials 2 LAB 3.4.1.13 Days of the week

class WeekDayError(Exception):
    pass
	

class Weeker:
    # This class is able to store and to manipulate days of a week
    # It uses dictionary to store names of the days
    days_week = {"Mon": 1,
                 "Tue": 2,
                 "Wed": 3,
                 "Thu": 4,
                 "Fri": 5,
                 "Sat": 6,
                 "Sun": 7}

    def __init__(self, day):
        # This constructor initialises object with current day
        # and raises exception if day is not in "Mon Tue Wed Thu Fri Sat Sun"
        if day in Weeker.days_week:
            self.__day = day
        else:
            raise WeekDayError

    def __str__(self):
        # This method makes object printable
        return self.__day

    def add_days(self, n):
        # This method adds n to the current day
        current_day = Weeker.days_week[self.__day]               #search number of current day
        current_day += n % 7                                     #skip whole weeks 
        self.__day = list(Weeker.days_week.keys())[current_day-1]#search name of current day

    def subtract_days(self, n):
        # This method subtracts n from the current day
        current_day = Weeker.days_week[self.__day]               #search number of current day
        current_day -= n % 7                                     #skip whole weeks 
        self.__day = list(Weeker.days_week.keys())[current_day-1]#search name of current day


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

