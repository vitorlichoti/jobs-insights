from src.pre_built.sorting import sort_by
import pytest


@pytest.fixture
def jobs_for_sort_without_criteria():
    return [
        {"max_salary": 1000, "min_salary": 100, "date_posted": "2020-05-09"},
        {"max_salary": 2000, "min_salary": 10, "date_posted": "2020-05-08"},
        {"max_salary": 1200, "min_salary": 1010, "date_posted": "2020-05-10"},
    ]


@pytest.fixture
def max_salary_sort():
    return [
            {"max_salary": 2000, "min_salary": 10,
             "date_posted": "2020-05-08"},
            {"max_salary": 1200, "min_salary": 1010,
             "date_posted": "2020-05-10"},
            {"max_salary": 1000, "min_salary": 100,
             "date_posted": "2020-05-09"},
    ]


@pytest.fixture
def min_salary_sort():
    return [
        {"max_salary": 2000, "min_salary": 10, "date_posted": "2020-05-08"},
        {"max_salary": 1000, "min_salary": 100, "date_posted": "2020-05-09"},
        {"max_salary": 1200, "min_salary": 1010, "date_posted": "2020-05-10"},
    ]


@pytest.fixture
def date_posted_sort():
    return [
            {"max_salary": 1200, "min_salary": 1010,
             "date_posted": "2020-05-10"},
            {"max_salary": 1000, "min_salary": 100,
             "date_posted": "2020-05-09"},
            {"max_salary": 2000, "min_salary": 10,
             "date_posted": "2020-05-08"},
    ]


def test_sort_by_criteria(jobs_for_sort_without_criteria, max_salary_sort,
                          min_salary_sort, date_posted_sort):
    keys = ['max_salary', 'date_posted', 'min_salary']
    criteria_keys = {
        "date_posted": date_posted_sort,
        "max_salary": max_salary_sort,
        "min_salary": min_salary_sort,
    }
    for key in keys:
        sort_by(jobs_for_sort_without_criteria, key)
        assert criteria_keys[key] == jobs_for_sort_without_criteria
