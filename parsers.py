# TODO: Remove obsolete parsing functions
from typing import List
from classes import TestCase, Job


def parse_input_file(filepath: str):
    # TODO: This is not working code, just a placeholder for the algorithm execution

    """Parses input file in format given as:
    ```
    n/1
    1. sustav
    t = [5, 6, 8,20, 1]
    d = [7,10,18,40,35]
    ```
        where:
      - n. sustav = the current test case
      - t = a list of processing times for given jobs
      - d = deadlines for given jobs

    or as:

    `n/m
    1. sustav, M = 29
    J = [[(1,5),(2,10),(3,7)], [(2,1),(3,8),(1,10)], [(3,5),(2,10),(1,4)]]

            where:
      - i. sustav = the i-th test case
      - M =  optimal makespan of the optimized system - for later grading
      - J = a list of lists of tuples, where each sublist represents a job made up of k tuples,
        each tuple being an operation on a given machine (tuple[0]), with given duration (tuple[1])
    """
    with open(filepath, 'r') as f:
        lines = f.readlines()

    test_cases = []

    for i, line in enumerate(lines):
        if line.startswith('n/1'):
            # parse test cases from this line onwards or until next 'n/1' or 'n/m' line
            parse_test_cases(lines[i+1:], system_type='n/1')
    return test_cases


def parse_test_case(lines: str):
    # TODO: Validate parsing, not tested

    """Parses test case from given lines.
    Example:
          1. sustav
          t = [ 5, 6]
          d = [12,20]

    should return:
    TestCase(system_type='n/1', test_case_number=1, jobs=[Job(due_date=12, processing_time=5),
                                                          Job(due_date=20, processing_time=6)])
    """
    for i,line in enumerate(lines):
        if "sustav" in line:
            # New test case
            jobs: List[Job] = []
            test_case_number = int(line.split(' ')[0].split('.')[0])

            if 'M' in line:
                system_type = 'n/m'
                makespan = parse_makespan(line)
            else:
                system_type = 'n/1'


            test_case = TestCase(system_type=system_type, test_case_number=test_case_number, jobs=jobs)

        elif line.startswith('t = '):
            # parse all values as a list of ints using list comprehension
            processing_times = [int(token.strip()) for token in line.split('=')[1].strip()[1:-1].split(',')]

        elif line.startswith('d = '):
            # parse all values as a list of ints using list comprehension
            deadlines = [int(token.strip()) for token in line.split('=')[1].strip()[1:-1].split(',')]

        elif line.startswith('J = '):
            # TODO: Add parsing for n/m test cases (can be across several lines)
            jobs = None
            jobs = parse_nm_jobs(lines[i:])
            pass

        if deadlines and processing_times:
            test_case.add_jobs(create_n1_jobs(deadlines, processing_times))
            return test_case

        if jobs:
            test_case.add_jobs(jobs)
            return test_case


def parse_test_cases(lines: List[str], system_type: str):
    test_cases: List[TestCase] = []
    current_test_case: TestCase
    # TODO: OVO NIJE GOTOVO, TRENUTNO JE CIJELA FUNKCIJA REDUDANTNA!
    # bit cu pametniji ujutro

    for i, line in enumerate(lines):
            test_cases.append(parse_test_case(lines[i:]))
        else:
            raise ValueError(f"Test case format mismatch for given system type {system_type} and current ")


        if current_test_case is not None:
            test_cases.append(current_test_case)
            current_test_case = []
        current_test_case.append(line)

    # Add the last test case if it wasn't added in the loop
    if current_test_case:
        test_cases.append(current_test_case)

    return test_cases


def parse_makespan(line: str) -> int:
    token = line.split('=')[1].strip()
    try:
        return int(token)
    except ValueError:
        raise ValueError(f"Invalid makespan value '{token}' in line {line}")


def create_n1_jobs(deadlines: List[int], processing_times: List[int]) -> List[Job]:
    """Creates a list of jobs from given deadlines and processing times."""
    jobs: List[Job] = []
    for deadline, processing_time in zip(deadlines, processing_times):
        jobs.append(Job(due_date=deadline, processing_time=processing_time))
    return jobs

def parse_nm_jobs(lines: str):
    # TODO: Validate parsing, not teste
    # TODO: Check what type this should return
    """Parses jobs from given lines, e.g.:
    J = [[(1,5),(2,4),(3,7),(4,18),(5,6),(6,10)], [(2,8),(6,13),(3,3),(4,5),(1,10),(5,6)],
         [(2,6),(3,14),(6,7),(1,7),(5,5),(4,4)], [(4,6),(5,7),(2,8),(1,2),(3,7),(6,15)]]
    """
    jobs = []
    job = []
    for line in lines:
        # parse given jobs from first line
        pass

        # in case current line ends with `,`, parse next line as well
        pass



