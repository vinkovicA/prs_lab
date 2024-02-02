"""
Laboratorijska vježba iz kolegija Projektiranje robotiziranih sustava.

Autori:
    - Pero Drobac,   0036523011
    - Ante Vinković, 0246080077

"""

from classes import Job
from typing import List


def sort_jobs_edd(jobs: List[Job]) -> List[Job]:
    """Earliest Due Date (EDD) algorithm, sorting jobs by `due_date` attribute in ascending order.
    """
    return sorted(jobs, key=lambda job: job.due_date)


def sort_jobs_spt(jobs: List[Job]) -> List[Job]:
    """Shortest Processing Time (SPT) algorithm, sorting jobs by `processing_time` attribute in ascending order.
    """
    return sorted(jobs, key=lambda job: job.processing_time)


def sort_jobs_moores(jobs: List[Job]) -> List[Job]:
    """ Sort jobs using Moore-Hodgson's Algorithm. Goal of the algorithm is to minimize the number of late jobs.
    Prioritizes equal jobs using EDD and SPT algorithms.
    """
    # K1: Init job lists, sort `non_late_jobs` by due date
    sorted_non_late_jobs = sort_jobs_edd(jobs)
    late_jobs = []

    # K2: Find the first job in `sorted_non_late_jobs` that is late
    job_to_remove_idx = None
    while True:
        if job_to_remove_idx is not None:
            # Remove the longest job found within the first i jobs from `sorted_non_late_jobs` and add it to `late_jobs`
            late_jobs.append(sorted_non_late_jobs.pop(job_to_remove_idx))

        # reset flag and time counter
        current_time = 0
        job_to_remove_idx = None
        for i, job in enumerate(sorted_non_late_jobs):
            current_time += job.processing_time
            if current_time > job.due_date:
                # Job is late, find the longest job within first `i` `sorted_non_late_jobs` entries
                job_to_remove_idx = find_longest_job_idx(sorted_non_late_jobs[:i+1])
                break

        if job_to_remove_idx is None:
            # No late jobs found, algorithm is finished
            break

    return sorted_non_late_jobs + late_jobs


def find_longest_job_idx(jobs: List[Job]) -> int:
    """Returns the index of the job with the longest processing time from the list of jobs. Prioritize the job with the
    earliest due date in case of equal processing times.
    """

    longest_job_idx = 0
    longest_job_time = 0

    for i, job in enumerate(jobs):
        if job.processing_time > longest_job_time:
            longest_job_time = job.processing_time
            longest_job_idx = i
        elif job.processing_time == longest_job_time:
            # Prioritize the job with the earliest due date
            if job.due_date < jobs[longest_job_idx].due_date:
                longest_job_idx = i

    return longest_job_idx

def calculate_starting_times(jobs: List[Job]) -> List[int]:
    """Outputs the starting times of the jobs in the list, based on their order and processing times.

    e.g. for sorted jobs with processing times [10,15,20] the output would be [0,10,25]
    """
    starting_times = []
    current_time = 0
    for job in jobs:
        starting_times.append(current_time)
        current_time += job.processing_time

    return starting_times
def sort_jobs_mwkr(jobs: List[Job]):
    """
    Implement MWKR priority-based heuristic algorithm. MWKR prioritizes with the most work remaining (MWR) heuristic.
    """
    pass


def calculate_remaining_work(job: Job, time) -> int:
    pass


def execute_algorithm(test_case):
    # TODO: This is not working code, just a placeholder for the algorithm execution
    if isinstance(test_case, TestCaseN1):
        result = spt_algorithm(test_case.t, test_case.d)
    elif isinstance(test_case, TestCaseNM):
        result = mwkr_algorithm(test_case.J)
    return result

def main():
    file_path = 'test_sustavi.txt'
    test_cases = parse_input(file_path)

    for idx, test_case in enumerate(test_cases, start=1):
        # TODO: This is not working code, just a placeholder for the algorithm execution

        print(f'Test Case {idx}:')
        result = execute_algorithm(test_case)
        print(result)
        print()


def local_test():
    # Create 3 jobs and sort them using EDD, SPT and Moores algorithms
    jobs = [Job(19, 10), Job(20, 20), Job(35, 15)]
    print('Original jobs:')
    print(jobs)
    print()

    print('Sorted by EDD:')
    print(sort_jobs_edd(jobs))
    print(f"s={calculate_starting_times(sort_jobs_edd(jobs))}")
    print()

    print('Sorted by SPT:')
    print(sort_jobs_spt(jobs))
    print(f"s={calculate_starting_times(sort_jobs_spt(jobs))}")
    print()

    print('Sorted by Moores:')
    print(sort_jobs_moores(jobs))
    print(f"s={calculate_starting_times(sort_jobs_moores(jobs))}")


if __name__ == "__main__":
    local_test()

