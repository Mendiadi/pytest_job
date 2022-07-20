"""
    Adi Mendel HomeWork
    1/7/22
    Sela Automation
"""
import statistics

def split_male_female(data_set: dict) -> [dict[int, (int, str)], dict[int, (int, str)]]:
    """
    This method take dict of dicts and return two dicts
    split by gender
    :param data_set: dict of dicts
    :return: two dicts of dicts
    """
    sex_key = "sex"
    male_sex = "male"
    female_sex = "female"
    female_dict = {}
    male_dict = {}
    index_key = 1
    for d in data_set.values():
        if isinstance(d, dict):  # for exam : list,int, etc value in data_set will crush function (optimal)
            if d.get(sex_key,0) == male_sex:
                    male_dict[index_key] = d
            if d.get(sex_key,0) == female_sex:
                    female_dict[index_key] = d
        index_key += 1
    return male_dict, female_dict


def get_median_average(data_set: dict) -> dict[str, float]:
    """
    Calculate average , median of given dict values
    :param data_set: dict of dicts
    :return: median and average store in dict
    """
    sum_of_ages = 0
    amount = 0  # To count values instead of call len(data_set)
    key_age = "age"
    median_list = []
    for d in data_set.values():
        if d.get(key_age, 0):
            if isinstance(d[key_age], (int, float)) and d[key_age] >= 0:  # Check if d["age"] is int, float (Optimal -
                # can remove that)
                sum_of_ages += d[key_age]
                median_list.append(d[key_age])
                amount += 1
    if amount == 0:
        return {"average": 0, "median": 0}
    average = sum_of_ages / amount
    print(median_list)
    median = statistics.median(median_list)
    return {"average": average, "median": median}


def print_values_above(data_set: dict, num: int = None) -> None:
    """
    Prints all values that "age" field above num.
    :param data_set: dict to print
    :param num: optimal - positive number
    :return: None
    """
    if num is None:
        num = 0
    if not isinstance(num, (int, float)):
        print("Second argument must be positive number type.")
        return
    if num < 0:
        return
    age_key = "age"
    for d in data_set.values():
        if d.get(age_key, 0):
            if isinstance(d[age_key], (int, float)):  # Check if d["age"] is int, float (Optimal - can remove that)
                if d[age_key] > num:
                    print(d)


def main():
    data_set = {
        1: {"name": "adi", "age": 23, "sex": "male"},
        2: {"name": "tal", "age": 21, "sex": "female"},
        3: {"name": "eden", "age": 45, "sex": "male"},
        4: {"name": "eyal", "age": 16, "sex": "male"},
        5: {"name": "gad", "age": 36, "sex": "female"},
    }
    """
        Debug tests if all dict have at least 3 elements (name,sex,age) optimal.
        Just for me messing with that, the exrcise assumed the input valid.
    """
    try:
        for d in data_set.values():
            assert d.get("age",0) and d.get("sex",0) and d.get("name")
    except AssertionError:
        print("Input Error "
              "Dict doesnt have at least 3 elements (name, sex, age)\n")

    result, result1 = split_male_female(data_set)
    print(f"Exercise 1:\nMales:\n{result}\nFemales:\n{result1}\n\n")
    print(f"Exercise 2:\n{get_median_average(data_set)}\n\n")
    print("Exercise 3:\n")
    print_values_above(data_set)


if __name__ == '__main__':
    main()
