from typing import List, Dict
import csv


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    unique_industries = []
    with open(path, 'r') as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        for job in jobs_reader:
            if job['industry'] not in unique_industries:
                if job['industry'] != '':
                    unique_industries.append(job['industry'])
    return unique_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    if industry == '':
        return []
    industry_filter = [job for job in jobs if industry in job['industry']]

    return industry_filter
