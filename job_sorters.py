"""
Laboratorijska vježba iz kolegija Projektiranje robotiziranih sustava.

Autori:
    - Pero Drobac,   0036523011
    - Ante Vinković, 0246080077

"""
from parsers import parse_input_file
from classes import *
from typing import List
import copy


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
                job_to_remove_idx = find_longest_job_idx(sorted_non_late_jobs[:i + 1])
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

def sort_nm_jobs_mwkr(jobs: List[JobNM], return_st_time : bool) -> List[JobNM]:
    """
    Implement MWKR priority-based heuristic algorithm. MWKR prioritizes with the most work remaining (MWR) heuristic.
    """
    num_of_machines = 0
    for job in jobs:
        for operation in job.operations:
            if operation.machine > num_of_machines:
                num_of_machines = operation.machine

    machine_timelines = [0] * num_of_machines

    machine_jobs = []
    for i in range(num_of_machines):
        machine_jobs.append([])

    starting_times = []
    for i in range(num_of_machines):
        starting_times.append([])

    done_flag = False
    t = 0
    while(not(done_flag)):
        #print()
        #print('NEW ITERATION, JOBS:')
        next_operations = []
        for job in jobs:
            # Fetch all ready operations
            if len(job.operations) != 0:
                next_operations.append(job.operations[0])
                #print(f'{job.operations[0]}')
            else:
                next_operations.append(False)
                #print(f'False')

        #print('Machine timelines:')
        #for i in range(len(machine_timelines)):
        #    print(f'Machine {i + 1}: {machine_timelines[i]}')

        # Check if done
        done_flag = True
        inner_done_flag = False
        for operation in next_operations:
            if operation != False:
                done_flag = False
                inner_done_flag = False
                break

        #print(f't = {t}')
        t2 = 0
        available_machines = [False] * num_of_machines
        for i in range(num_of_machines):
            if machine_timelines[i] <= t:
                available_machines[i] = True

        while(not(inner_done_flag)):
            inner_done_flag = True
            for i in range(len(jobs)):
                if next_operations[i] == False:
                    continue
                machine = next_operations[i].machine - 1
                if available_machines[machine]:
                    inner_done_flag = False
                if (jobs[i].processing_time() <= t2) and available_machines[machine]:
                    # Commit to job
                    machine_jobs[machine].append(next_operations[i])
                    st_time = machine_timelines[machine]
                    starting_times[machine].append(st_time)
                    machine_timelines[machine] = st_time + next_operations[i].processing_time
                    removed = jobs[i].operations.pop(0)
                    available_machines[machine] = False
                    #print(f'Accepted operation {removed}')
            t2 += 1
        
        t += 1

    if return_st_time:
        return starting_times
    return machine_jobs


def sort_nm_jobs_spt(jobs: List[JobNM], return_st_time) -> List[JobNM]:
    """
    Implement SPT priority-based heuristic algorithm. SPT prioritizes with the shortest processing time (SPT) heuristic.
    """ 
    num_of_machines = 0
    for job in jobs:
        for operation in job.operations:
            if operation.machine > num_of_machines:
                num_of_machines = operation.machine

    machine_timelines = [0] * num_of_machines

    machine_jobs = []
    for i in range(num_of_machines):
        machine_jobs.append([])

    starting_times = []
    for i in range(num_of_machines):
        starting_times.append([])

    done_flag = False
    t = 0
    while(not(done_flag)):
        #print()
        #print('NEW ITERATION, JOBS:')
        next_operations = []
        for job in jobs:
            # Fetch all ready operations
            if len(job.operations) != 0:
                next_operations.append(job.operations[0])
                #print(f'{job.operations[0]}')
            else:
                next_operations.append(False)
                #print(f'False')

        #print('Machine timelines:')
        #for i in range(len(machine_timelines)):
        #    print(f'Machine {i + 1}: {machine_timelines[i]}')

        # Check if done
        done_flag = True
        inner_done_flag = False
        for operation in next_operations:
            if operation != False:
                done_flag = False
                inner_done_flag = False
                break

        #print(f't = {t}')
        t2 = t
        available_machines = [False] * num_of_machines
        for i in range(num_of_machines):
            if machine_timelines[i] <= t:
                available_machines[i] = True

        while(not(inner_done_flag)):
            inner_done_flag = True
            for i in range(len(jobs)):
                if next_operations[i] == False:
                    continue
                machine = next_operations[i].machine - 1
                if available_machines[machine]:
                    inner_done_flag = False
                if (machine_timelines[machine] + next_operations[i].processing_time <= t2) and available_machines[machine]:
                    # Commit to job
                    machine_jobs[machine].append(next_operations[i])
                    st_time = max(machine_timelines[machine], t2)
                    starting_times[machine].append(st_time - next_operations[i].processing_time)
                    machine_timelines[machine] = st_time + next_operations[i].processing_time
                    removed = jobs[i].operations.pop(0)
                    available_machines[machine] = False
                    #print(f'Accepted operation {removed}')
            t2 += 1
        
        t += 1

    if return_st_time:
        return starting_times
    return machine_jobs


def calculate_remaining_work(job: Job, time) -> int:
    """Calculates the remaining work of the job at the given time. Used for MWKR algorithm."""
    # TODO: Maybe change the input arguments, this is a placeholder function prototype
    pass


def calculate_total_time(sorted_jobs: List[Job]) -> float:
    """Returns the sum of total times required to process all jobs in the list."""
    total_time = 0
    for job in sorted_jobs:
        total_time += (total_time + job.processing_time)
    return total_time


def calculate_ct(sorted_jobs: List[Job]) -> float:
    """Returns average cycle time as a sum of all processing times and all queue times, divided by the number of jobs"""
    total_time = calculate_total_time(sorted_jobs)
    return total_time / len(sorted_jobs)


def calculate_ct_uk(sorted_jobs: List[Job]) -> float:
    """Returns the sum of all processing times of the jobs in the list.
    Equivalent to the total time required to process all the jobs."""
    return sum(job.processing_time for job in sorted_jobs)


def calculate_ct_k(sorted_jobs: List[Job]) -> float:
    """Returns the sum of all queue times of the jobs in the list."""
    total_time = calculate_total_time(sorted_jobs)
    return total_time - calculate_ct_uk(sorted_jobs)    # ct_k = ct - ct_uk


def calculate_wip(sorted_jobs: List[Job]) -> float:
    ct = calculate_ct(sorted_jobs)
    th = len(sorted_jobs) / calculate_total_time(sorted_jobs)
    return ct * th


def print_job_stats(jobs: List[Job]) -> None:
    print(f"s = {calculate_starting_times(jobs)}")
    print(f"\tCT = {calculate_ct(jobs)}")
    print(f"\tCT_uk = {calculate_ct_uk(jobs)}")
    print(f"\tCT_k = {calculate_ct_k(jobs)}")
    print(f"\tWIP = {calculate_wip(jobs)}")
    print()


def run_n1(jobs: List[Job]) -> None:
    jobs_sorted_moores = sort_jobs_moores(jobs)
    jobs_sorted_edd = sort_jobs_edd(jobs)
    jobs_sorted_spt = sort_jobs_spt(jobs)

    print('Original jobs:')
    print(jobs)
    print()

    print('Sorted by EDD:')
    print_job_stats(jobs_sorted_edd)

    print('Sorted by SPT:')
    print_job_stats(jobs_sorted_spt)

    print('Sorted by Moores:')
    print_job_stats(jobs_sorted_moores)

    print("- - - - - - - - - - - - -\n")


def run_nm(jobs: List[JobNM]) -> None:
    print('Original jobs:')
    print(jobs)
    print()

    jobs_mwkr_1 = copy.deepcopy(jobs)
    jobs_mwkr_2 = copy.deepcopy(jobs)
    jobs_spt_1 = copy.deepcopy(jobs)
    jobs_spt_2 = copy.deepcopy(jobs)

    print('Sorted using heuristics with MWKR priority:')
    print("- - Machine jobs - -")
    print(sort_nm_jobs_mwkr(jobs_mwkr_1, False))
    print("- - Starting_times - -")
    print(f"s={sort_nm_jobs_mwkr(jobs_mwkr_2, True)}")

    print('Sorted using heuristics with SPT priority:')
    print("- - Machine jobs - -")
    print(sort_nm_jobs_spt(jobs_spt_1, False))
    print("- - Starting_times - -")
    print(f"s={sort_nm_jobs_spt(jobs_spt_2, True)}")

    print("- - - - - - - - - - - - -\n")


def execute_algorithms(test_cases):
    for tc in test_cases:
        if tc.system_type == 'n/1':
            run_n1(tc.jobs)
        elif tc.system_type == 'n/m':
            run_nm(tc.jobs)


def main():
    file_path = 'input/test_nm.txt'
    test_cases = parse_input_file(file_path)
    execute_algorithms(test_cases)


def local_test():
    # Create 3 jobs and sort them using EDD, SPT and Moores algorithms
    jobs = [Job(due_date=19, processing_time=10),
            Job(due_date=20, processing_time=20),
            Job(due_date=35, processing_time=15)]
    run_n1(jobs)

    #jobs = [JobNM(operations=[Operation(machine=1, processing_time=10), Operation(machine=2, processing_time=1)]),
    #        JobNM(operations=[Operation(machine=1, processing_time=2), Operation(machine=2, processing_time=20)])]
    #run_nm(jobs)


if __name__ == "__main__":
    # local_test()
    main()
