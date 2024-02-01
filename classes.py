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
    def __init__(self, jobs: List[Job], system_type: str):
        if system_type == 'n/1' or system_type == 'n/m':
            self.jobs = jobs
        else:
            raise ValueError('Invalid system type.')


class TestCaseN1(TestCase):
    def __init__(super, t, d):
        self.t = t
        self.d = d


class TestCaseNM(TestCase):
    def __init__(self, M, J):
        self.M = M
        self.J = J

