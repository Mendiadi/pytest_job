from homework4 import Date
import pytest
import logging

LOGGER = logging.getLogger("__name__")


@pytest.fixture
def get_valid_date() -> Date:
    """
    init valid date
    :return: valid date
    """
    return Date(25, 11, 1998)


def test_sub_type_check(get_valid_date):
    """
    Test type checking for sub
    :param get_valid_date:
    :return:
    """
    LOGGER.info("testing case trying to sub with other types")
    with pytest.raises(TypeError):
        assert get_valid_date - 3


@pytest.mark.parametrize("self,other,excepted",
                         [(Date(30, 8, 2012), Date(23, 8, 2012), 7),
                          (Date(11, 8, 2012), Date(2, 8, 2010), 740),
                          (Date(11, 8, 2012), Date(11, 8, 2012), 0)])
def test_sub_function(self, other, excepted):
    """
    Testing sub functional with different valid inputs
    :param self: date
    :param other: date
    :param excepted: should output
    :return:
    """
    LOGGER.info("test sub functionality")
    assert self - other == excepted


@pytest.mark.parametrize("self,other,excepted",
                         [(Date(11, 8, 2012), Date(23, 8, 2012), False),
                          (Date(11, 8, 2012), Date(2, 8, 2010), True),
                          (Date(11, 8, 2012), Date(11, 8, 2012), True)])
def test_greater_then_and_equal(self, other, excepted):
    """
    Testing greater then and equal functional with different valid inputs
    :param self: date
    :param other: date
    :param excepted: should output
    :return:
    """
    LOGGER.info("test greater then and equal functionality")
    assert (self >= other) == excepted


@pytest.mark.parametrize("self,other,excepted",
                         [(Date(11, 8, 2012), Date(23, 8, 2012), True),
                          (Date(11, 8, 2012), Date(2, 8, 2010), False),
                          (Date(11, 8, 2012), Date(11, 8, 2012), True)])
def test_lower_then_and_equal(self, other, excepted):
    """
    Testing lower then and equal functional with different valid inputs
    :param self: date
    :param other: date
    :param excepted: should output
    :return:
    """
    LOGGER.info("test lower then and equal functionality")
    assert (self <= other) == excepted


@pytest.mark.parametrize("date,other,excepted", [(Date(20, 5, 2020), Date(20, 5, 2020), False),
                                                 (Date(21, 5, 2020), Date(22, 5, 2020), True)])
def test_not_equal_dates(date, other, excepted):
    """
    Test if not equal operator works
    :return:
    """
    LOGGER.info("test not equal functional")
    assert (date != other) is excepted


@pytest.mark.parametrize("date,other,excepted", [(Date(20, 5, 2020), Date(20, 5, 2020), True),
                                                 (Date(21, 5, 2020), Date(22, 5, 2020), False),
                                                 (Date(19, 5, 2020), Date(15, 5, 2020), False)])
def test_equal_dates(date, other, excepted):
    """
    Test if equal operator works
    :return:
    """
    LOGGER.info("test equal functional")
    assert (date == other) is excepted


def test_date_init_and_str_work(get_valid_date):
    """
    Test if date init done correctly with valid date
    :param get_valid_date: valid date
    :return:
    """
    LOGGER.info("test case date init valid")
    assert get_valid_date.__str__() == "25/11/1998"


def test_GetNextDays_raises_type(get_valid_date):
    """
    Test getNextDays with invalid type param
    :param get_valid_date:
    :return:
    """
    LOGGER.info("test case date init invalid")
    with pytest.raises(TypeError):
        get_valid_date.getNextDays("dd")


def test_getNextDays(get_valid_date):
    """
    Test getNextDays with valid input
    :param get_valid_date:
    :return:
    """
    LOGGER.info("test getNextDays functionality")
    assert get_valid_date.getNextDays(10).__str__() == "5/12/1998"


@pytest.mark.parametrize("self,other,excepted",
                         [(Date(11, 8, 2012), Date(23, 8, 2012), True),
                          (Date(11, 8, 2012), Date(2, 8, 2010), False),
                          (Date(11, 8, 2012), Date(11, 8, 2012), False),
                          (Date(30, 8, 2012), Date(23, 8, 2012), False)])
def test_lower_then(self, other, excepted):
    """
    Testing lower then functional with different valid inputs
    :param self: date
    :param other: date
    :param excepted: should output
    :return:
    """
    LOGGER.info("test lower then functionality")
    assert (self < other) == excepted


@pytest.mark.parametrize("self,other,excepted",
                         [(Date(11, 8, 2012), Date(23, 8, 2012), False),
                          (Date(11, 8, 2012), Date(2, 8, 2010), True),
                          (Date(11, 8, 2012), Date(11, 8, 2012), False),
                          (Date(30, 8, 2012), Date(23, 8, 2012), True)])
def test_greater_then(self, other, excepted):
    """
        Testing greater then functional with different valid inputs
        :param self: date
        :param other: date
        :param excepted: should output
        :return:
    """
    LOGGER.info("test lower then functionality")
    assert (self > other) == excepted


@pytest.mark.parametrize("day,mouth,year,expected",
                         [(28, 2, 2005, "1/3/2005"), (28, 2, 2012, "29/2/2012"), (31, 12, 1998, "1/1/1999"),
                          (23, 11, 2000, "24/11/2000")])
def test_GetNextDay(day, mouth, year, expected):
    """
    Test getNextDay function with different cases
    :param day: day input
    :param mouth: mouth input
    :param year: year input
    :param expected: excepted result
    :return:
    """
    LOGGER.info("testing cases input and functionality to getNextDay")
    assert Date(day, mouth, year).getNextDay().__str__() == expected


@pytest.mark.parametrize("day,mouth,year",
                         [(29, 2, 2005), (30, 2, 1998), (31, 9, 1998)])
def test_date_isvalid_detect_correctly(day, mouth, year):
    """
    Test if __isvalid function detect all invalid dates
    :param day:
    :param mouth:
    :param year:
    :return:
    """
    LOGGER.info("test invalid input handle")
    with pytest.raises(BaseException):
        Date(day, mouth, year)


@pytest.mark.parametrize("day,mouth,year",
                         [(35, 11, 1998), (30, 14, 1998), (1, 1, 11998), (1, 1, 198), ("1", "23", "3323")])
def test_init_date_raise_type_exception(day, mouth, year):
    """
    Test if date init checking types
    :param day:
    :param mouth:
    :param year:
    :return:
    """
    LOGGER.info("verify if there are type checking")
    with pytest.raises(TypeError):
        Date(day, mouth, year)
