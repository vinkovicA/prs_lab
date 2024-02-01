# TODO: Remove obsolete parsing functions

def parse_input_file(filepath: str):
    # TODO: This is not working code, just a placeholder for the algorithm execution

    """Parses input file in format given as:

    'n/1
    1. sustav
    t = [5, 6, 8,20, 1]
    d = [7,10,18,40,35]'

        where:
      - n. sustav = the current test case
      - t = a list of processing times for given jobs
      - d = deadlines for given jobs

    or as:

    `n/m
    1. sustav, M = 29
    J = [[(1,5),(2,10),(3,7)], [(2,1),(3,8),(1,10)], [(3,5),(2,10),(1,4)]]

            where:
      - n. sustav = the current test case
      - M =  optimal makespan of the optimized system
      - J = a list of lists of tuples, where each sublist represents a job made up of k tuples,
        each tuple being an operation on a given machine (tuple[0]), with given duration (tuple[1])
    `

    Multiple test cases are contained in one file, with same system cases being preceded either by 'n/1' or 'n/m'. The following line enumerates the test case for given type.
    E.g.:
    `n/1
    1. sustav
    t = [5, 6, 8,20, 1]
    d = [7,10,18,40,35]

    2. sustav
    t = [5, 6, 8,20, 1,50,16, 5]
    d = [7,15,20,50,25,70,50,21]

    3. sustav
    t = [ 5, 6, 8,20,10,21,17, 2,40,35,25]
    d = [12,20,13,30,40,60,90,50,45,75,27]

    4. sustav
    t = [ 5, 6, 8,20,14,21, 30, 99,50,45, 3,20, 15, 17, 30, 40, 15, 25,30,35, 4]
    d = [12,20,23,40,40,80,100,200,85,75,79,99,115,105,250,175,300,190,70,45,60]


    n/m
    1. sustav, M = 29
    J = [[(1,5),(2,10),(3,7)], [(2,1),(3,8),(1,10)], [(3,5),(2,10),(1,4)]]

    2. sustav, M = 24
    J = [[(1,5),(2,3),(3,4),(4,2)], [(3,4),(2,5),(1,6)],[(4,6),(2,5),(3,7)]]

    3. sustav, M = 44
    J = [[(1,5),(2,4),(3,7),(4,8),(5,6)], [(2,8),(3,3),(4,5),(1,10),(5,6)],[(5,10),(4,2),(3,3),(2,4),(1,5)],
         [(2,6),(3,4),(1,7),(5,5),(4,4)], [(4,6),(5,7),(2,8),(1,2),(3,7)]]

    4. sustav, M = 65
    J = [[(1,5),(2,4),(3,7),(4,18),(5,6),(6,10)], [(2,8),(6,13),(3,3),(4,5),(1,10),(5,6)],[(5,10),(4,12),(6,6),(3,3),(2,4),(1,5)],
         [(2,6),(3,14),(6,7),(1,7),(5,5),(4,4)], [(4,6),(5,7),(2,8),(1,2),(3,7),(6,15)]]
    `
    Creates a list of JobSorter objects, each representing a test case.
    """
    with open(filepath, 'r') as f:
        lines = f.readlines()

    test_cases = []

    for line in lines:
        if line.startswith('n/1'):
            pass

        elif line.startswith('n/m'):
            pass

        elif line.startswith('J = '):
            pass

        elif line.startswith('t = '):
            pass

        elif line.startswith('d = '):
            pass

        elif line.startswith('M = '):
            pass

        elif 'sustav' in line:
            pass
    return test_cases

def parse_jobs(line: str):
    # TODO: Validate parsing, not tested
    """Parses jobs from given line."""
    jobs = []
    job = []
    for char in line:
        if char == '(':
            job.append([])
        elif char == ')':
            jobs.append(job)
            job = []
        elif char.isdigit():
            job[-1].append(int(char))
    return jobs

def parse_processing_times(line: str):
    # TODO: Validate parsing, not tested

    """Parses processing times from given line."""
    processing_times = []
    for char in line:
        if char.isdigit():
            processing_times.append(int(char))
    return processing_times

def parse_deadlines(line: str):
    # TODO: Validate parsing, not tested

    """Parses deadlines from given line."""
    deadlines = []
    for char in line:
        if char.isdigit():
            deadlines.append(int(char))
    return deadlines

def parse_M(line: str):
    # TODO: Validate parsing, not tested

    """Parses M from given line."""
    return int(line.split('=')[1])

def parse_test_case(line: str):
    # TODO: Validate parsing, not tested

    """Parses test case from given line."""
    return int(line.split('.')[0])
