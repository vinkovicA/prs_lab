from typing import List


class Job:
    # TODO: Either rename this class to `JobN1` and create a new class `JobNM` or expand this class to support both
    due_date: int
    processing_time: int

    def __init__(self, due_date: int, processing_time: int):
        self.due_date = due_date
        self.processing_time = processing_time

    def __repr__(self):
        return f'Job of length: {self.processing_time}, \tdue: {self.due_date})'


class TestCase:
    def __init__(self, system_type: str, test_case_number: int, jobs: List[Job] = None):
        if system_type == 'n/1' or system_type == 'n/m':
            self.system_type = system_type
            self.test_case_number = test_case_number

            if jobs is None:
                self.jobs = []
            else:
                self.jobs = jobs
        else:
            raise ValueError('Invalid system type.')

    def __repr__(self):
        return f'Test case {self.test_case_number} of type with {len(self.jobs)} jobs.'

    def add_job(self, job: Job):
        self.jobs.append(job)

    def add_jobs(self, jobs: List[Job]):
        self.jobs.extend(jobs)


class TestCaseN1(TestCase):
    def __init__(super, t, d):
        self.t = t
        self.d = d


class TestCaseNM(TestCase):
    def __init__(self, M, J):
        self.M = M
        self.J = J

