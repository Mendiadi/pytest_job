"""
    Adi mendel pytest project
    test for home work 3
"""
import homwwork3
import pytest
import logging
import numpy
import statistics
LOGGER = logging.getLogger("__name__")


@pytest.fixture
def init_data() -> dict[dict]:
    """
        Giving data to test with
    :return: dict of dicts data
    """
    data = {
        1: {"name": "adi", "age": 23, "sex": "male"},
        2: {"name": "tal", "age": 21, "sex": "female"},
        3: {"name": "eden", "age": 45, "sex": "male"},
        4: {"name": "eyal", "age": 16, "sex": "male"},
        5: {"name": "gad", "age": 36, "sex": "female"}
    }
    print("connect to DB") # simulation
    yield data
    print("\nDisconnect DB") # simulation

@pytest.fixture
def get_all_ages_from_data(init_data) -> list[int]:
    """
    Init and return list of all ages
    :param init_data: the data
    :return: list of ages
    """
    l = [i['age'] for i in init_data.values()]
    return l


@pytest.fixture
def get_median_and_average(init_data) -> dict[str,float]:
    """
    Returning the median and average
    :param init_data: init data
    :return: dict of median and avg
    """
    return homwwork3.get_median_average(init_data)


@pytest.mark.smoke
@pytest.mark.parametrize("n",[(20),(15),(26),(None)])
def test_print_values_above(init_data, get_all_ages_from_data,capfd,n):
    """
    Testing if its print the age above n
    :param init_data: init dict
    :param get_all_ages_from_data: list of ages from init dict
    :param capfd: buffer to console
    :param n: print ages above n
    :return:
    """
    LOGGER.info("Test if print_value_above prints correctly")
    homwwork3.print_values_above(init_data,n)
    out = capfd.readouterr().out
    if n is None:
        n = 0
    for age in get_all_ages_from_data:
        assert str(age) in out if age > n else str(age) not in out


@pytest.mark.smoke
def test_male_and_female_split_correct(init_data):
    """
    Testing if function split correct
    :param init_data: init data
    :return:
    """
    LOGGER.info("inside male\\female split test")
    male,female = homwwork3.split_male_female(init_data)
    for k,v in init_data.items():
        if v.get("sex") == 'male':
            assert k in male
        if v.get("sex") == 'female':
            assert k in female



@pytest.mark.smoke
def test_median_result(get_median_and_average,get_all_ages_from_data):
    """
    test if median result correct
    :param get_median_and_average: median result
    :param get_all_ages_from_data: list of ages
    :return:
    """
    LOGGER.info("Testing if median calculate correctly")
    assert get_median_and_average['median'] == statistics.median(get_all_ages_from_data)

@pytest.mark.smoke
def test_average_result(get_median_and_average,get_all_ages_from_data):
    """
     test if average result correct
    :param get_median_and_average: median result
    :param get_all_ages_from_data: list of ages
    :return:
    """
    LOGGER.info("Testing if average calculate correctly")
    assert get_median_and_average['average'] == numpy.average(get_all_ages_from_data)


if __name__ == '__main__':
    pass