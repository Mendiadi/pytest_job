from __future__ import annotations

# __future__ to be able to make functions hints for Date class
# can also use "Date"


"""
    Adi Mendel HomeWork 4
"""


class Date:
    """
    Date class represent date data type
    """

    def __init__(self, day: int, month: int, year: int) -> None:
        """
        Constructor : initial data members
        :param day: numbers between 1-31
        :param mouth: numbers between 1-12
        :param year: number with 4 digits
        """
        if not isinstance(day, int) or day not in range(1, 32):
            raise TypeError("day param must be integer between 1-31")
        if not isinstance(month, int) or month not in range(1, 13):
            raise TypeError("mouth param must be integer between 1-12")
        if not isinstance(year, int) or not year in range(1000, 10000):
            raise TypeError("year param must be integer with 4 digits")
        self._year = year
        self._month = month
        self._day = day
        if not self.__isvalid():
            raise BaseException(f"Error invalid Date: {self} is not a valid date")

    def __str__(self) -> str:
        """

        :return: representing string
        """
        return f"{self._day}/{self._month}/{self._year}"

    def __isvalid(self) -> bool:
        """
        Check if date are valid
        :return: bool
        """
        mouths_that_has_31th_days = [1, 3, 5, 7, 8, 10, 12]
        mouths_that_has_30th_days = [4, 6, 9, 11]
        if self._day not in range(1, 31) and self._month in mouths_that_has_30th_days:
            return False
        if self._day not in range(1, 32) and self._month in mouths_that_has_31th_days:
            return False
        if self._day not in range(1, 30) and self._month == 2 and \
                (self._year % 4 == 0 and (self._year % 100 != 0 or self._year % 400 == 0)):
            return False
        if self._day not in range(1, 29) and self._month == 2 and not \
                (self._year % 4 == 0 and (self._year % 100 != 0 or self._year % 400 == 0)):
            return False
        return True

    def getNextDay(self) -> Date:
        """
        Calculate the date of current date + 1 day
        example: 12/1/2020 returns 13/1/2020
        :return: Date of next day
        """
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (self._year % 4 == 0) and (self._year % 400 == 0 or self._year % 100 != 0):
            month_days[1] = 29
        if self._day == month_days[self._month - 1]:
            if self._month == 12:
                return Date(1, 1, self._year + 1)
            else:
                return Date(1, self._month + 1, self._year)
        else:
            return Date(self._day + 1, self._month, self._year)

    def getNextDays(self, days_to_add: int) -> Date:
        """
        Returns the date after n days from current date
        example: given 12/4/2020 with 10 returns 22/4/2020
        :param days_to_add: number of days
        :return: date after n days
        """
        if not isinstance(days_to_add, int):
            raise TypeError("days_to_add param must be integer")
        date = self
        for i in range(days_to_add):
            date = date.getNextDay()
        return date

    def __eq__(self, other: Date) -> bool:
        """
        Checking if self date is equal to other date.
        :param other: other date
        :return: true if they equal
        """
        if not isinstance(other, Date):
            raise TypeError("other param: must be Date type")
        return self._year == other._year and self._month == other._month and self._day == other._day

    def __lt__(self, other: Date) -> bool:
        """
        Checking if self date lower then other date.
        :param other: other date
        :return: true if self date is lower.
        """
        if not isinstance(other, Date):
            raise TypeError("other param: must be Date type")
        if self._year == other._year:
            if self._month == other._month:
                return self._day < other._day
            else:
                return self._month < other._month
        else:
            return self._year < other._year

    def __gt__(self, other: Date) -> bool:
        """
        Checking if self date greater then other date.
        :param other: other date
        :return: true if grater then other
        """
        if not isinstance(other, Date):
            raise TypeError("other param: must be Date type")
        return not (self < other or self == other)

    def __ne__(self, other: Date) -> bool:
        """
        Check if self Date different then other date.
        :param other: other date
        :return: True is they not equal
        """
        if not isinstance(other, Date):
            raise TypeError("other param: must be Date type")
        return not self == other

    def __le__(self, other: Date) -> bool:
        """
        Check if self date is equal or lower then other.
        :param other: other Date
        :return: True if self date is lower or equal to other
        """
        if not isinstance(other, Date):
            raise TypeError("other param: must be Date type")
        return self == other or self < other

    def __ge__(self, other: Date) -> bool:
        """
        Check if self date is equal or greater then other.
        :param other: other Date
        :return: True if self date is greater or equal to other
        """
        if not isinstance(other, Date):
            raise TypeError("other param: must be Date type")
        return self == other or self > other

    def __sub__(self, other: Date) -> int:
        """
        Calculate returns the amount of days between self date to other,
        if the self date < other its will return negative value.
        :param other: other Date
        :return:  amount of days between self date to other
        """
        if not isinstance(other, Date):
            raise TypeError("other param: must be Date type")
        tuple_of_two_dates = (self, other)  # to avoid duplicate calculation (make "inDays()" method is better)
        mouths_days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # to figure how many days to add
        temp = []  # save the amount of days to each date
        for d in tuple_of_two_dates:
            days_count = (d._year * 365) + d._day
            year_count = d._year
            for mouth in range(d._month - 1):
                days_count += mouths_days[mouth]
            if d._month <= 2:
                year_count -= 1
            days_count += (int(year_count / 4) - int(year_count / 100) + int(year_count / 400))
            temp.append(days_count)
        return temp[0] - temp[1]


def main():
    date1 = Date(28, 2, 2016)
    date2 = Date(20, 3, 2020)
    date3 = Date(3, 7, 2020)
    date4 = Date(10, 7, 2020)
    print(f"next day of {date1} is {date1.getNextDay()}")
    print(f"next day of {date2} is {date2.getNextDay()}")
    print(f"{date2.getNextDays(10)} is 10 days after {date2}")
    print(f"is {date3} come to {date4} after one week (7 days)? {date3.getNextDays(7) == date4} ")
    print(f"{date3} == {date1} ? {date3 == date1}")
    print(f"{date3} != {date1} ? {date3 != date1}")
    print(f"{date1} > {date2} ? {date1 > date2}")
    print(f"{date1} >= {date4} ? {date1 >= date4}")
    print(f"{date3} < {date4} ? {date3 < date4}")
    print(f"{date3} <= {date4} ? {date3 <= date4}")
    print(f"{date4} - {date2} ? {date4 - date2} days")


if __name__ == '__main__':
    main()
