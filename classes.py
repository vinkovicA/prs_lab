from typing import List


class Operation:
    machine: int
    processing_time: int

    def __init__(self, machine: int, processing_time: int):
        self.machine = machine
        self.processing_time = processing_time

    def __repr__(self):
        return f'(m={self.machine}, t={self.processing_time})'


class JobNM:
    operations: List[Operation]

    def __init__(self, operations: List[Operation]=None):
        if operations is None:
            self.operations = []
        else:
            self.operations = operations

    def __repr__(self):
        return f'NM job  with {len(self.operations)} operations:\n{self.operations}\n'
    
    def processing_time(self):
        t = 0
        for operation in self.operations:
            t += operation.processing_time
        return t


class Job:
    # TODO: Either rename this class to `JobN1` and create a new class `JobNM` or expand this class to support both
    due_date: int
    processing_time: int

    def __init__(self, due_date: int, processing_time: int):
        self.due_date = due_date
        self.processing_time = processing_time

    def __repr__(self):
        return f'(t={self.processing_time}, d={self.due_date})'


class TestCase:
    def __init__(self, system_type: str, test_case_number: int, jobs: List = None, makespan: int = None):
        if system_type == 'n/1' or system_type == 'n/m':
            self.system_type = system_type
            self.test_case_number = test_case_number

            if jobs is None:
                self.jobs = []
            else:
                self.jobs = jobs

            if system_type == 'n/m':
                self.makespan = makespan
        else:
            raise ValueError('Invalid system type.')

    def __repr__(self):
        return f'Test case {self.test_case_number} of type {self.system_type} with {len(self.jobs)} jobs.'

    def add_job(self, job: Job):
        self.jobs.append(job)

    def add_jobs(self, jobs: List[Job]):
        self.jobs.extend(jobs)


class TestCaseN1(TestCase):
    def __init__(self, t, d):
        self.t = t
        self.d = d


class TestCaseNM(TestCase):
    def __init__(self, M, J):
        self.M = M
        self.J = J

