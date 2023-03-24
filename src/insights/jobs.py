from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    result = []
    with open(path, 'r') as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        for row in jobs_reader:
            result.append(row)
    return result


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    unique_jobs = []
    with open(path, 'r') as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        for row in jobs_reader:
            if row['job_type'] not in unique_jobs:
                unique_jobs.append(row['job_type'])
    return unique_jobs


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    jobs_filtered = []
    for job in jobs:
        if job['job_type'] == job_type:
            jobs_filtered.append(job)

    
    return jobs_filtered
