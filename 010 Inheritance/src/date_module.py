# This class is adapted a class from the book 'Building Python Programs'
# by Allison Obourn, Marty Stepp and Stuart Reges.
#
# A Date object represents a day, month and year such as 25/12/1999.
#
# Invariants:
# Every Date's month value is from 1-12 inclusive,
# and its day value is from 1 to # of days in its month inclusive.
#
# The year must be greater than or equal to EARLIEST_YEAR

class Date:
    EARLIEST_YEAR = 1999

    # Constructor initializes the state of new
    # Date objects as they are created by client code.
    # Raises a ValueError if values are out of range.
    def __init__(self, day, month, year):
        self.month = month
        self.day = day
        self.year = year

    # Returns a string representation of a Date, such as "9/19".
    def __str__(self):
        return str(self._day) + "/" + str(self._month) + "/" + str(self._year)

    # Compares two Date objects.
    def __eq__(self, otherDate):
        if isinstance(otherDate, Date):
            return self.day == otherDate.day and self.month == otherDate.month \
                   and self.year == otherDate.year
        else:
            raise TypeError("Argument must be a Date object.")

    # month property allows get/set access to Date's month value
    # must be between 1-12 inclusive, else a ValueError is raised
    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        if 1 <= value <= 12:
            self._month = value
        else:
            raise ValueError("Invalid month: " + str(value))

    # day property allows get/set access to Date's day value
    # must be between 1 - # of days in month, inclusive
    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        if 1 <= value <= self.days_in_month():
            self._day = value
        else:
            raise ValueError("Invalid day: " + str(value))

    # year property allows get/set access to Date's year value
    # must be an integer greater than 1990
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if value >= self.EARLIEST_YEAR:
            self._year = value
        else:
            raise ValueError

    # Returns the number of days in this Date's month.
    def days_in_month(self):
        if self.month in {4, 6, 9, 11}:
            return 30
        elif self.month == 2:
            return 28
        else:
            return 31

    # Modifies the date's day, month and year state.
    # Raises a ValueError if values are out of range.
    def set_date(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
