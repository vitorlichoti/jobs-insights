from typing import Union, List, Dict
import csv


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    salary = []
    with open(path, 'r') as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        for jobs in jobs_reader:
            if jobs['max_salary'] != '' and not jobs['max_salary'].isalpha():
                salary.append(int(jobs['max_salary']))

    return max(salary)


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    salary = []
    with open(path, 'r') as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        for jobs in jobs_reader:
            if jobs['min_salary'] != '' and not jobs['min_salary'].isalpha():
                salary.append(int(jobs['min_salary']))

    return min(salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if 'min_salary' not in job or 'max_salary' not in job:
        raise ValueError('As chaves sao obrigatorias')
    if not isinstance(
            job['min_salary'],
            Union[int, str]) or not isinstance(
                job['max_salary'],
                Union[int, str]) or not isinstance(salary, Union[int, str]):
        raise ValueError('Os valores devem ser numericos')
    if int(job['min_salary']) > int(job['max_salary']):
        raise ValueError('min_salary é maior que max_salary')
    if int(salary) >= int(job['min_salary']) and int(salary) <= int(
                job['max_salary']):
        return True
    else:
        return False


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
