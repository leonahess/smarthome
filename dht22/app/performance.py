import datetime


class Performance:

    def __init__(self):
        pass

    def program_start(self):
        self.start_time = datetime.datetime.utcnow()

    def cycle_start(self):
        self.cycle_start_time = datetime.datetime.utcnow()

    def cycle_end(self):
        self.cycle_end_time = datetime.datetime.utcnow()

    def program_runtime(self):
        self.run_time = (datetime.datetime.utcnow() - self.start_time).total_seconds()

    def calc_cycle_time(self):
        self.cycle_time = (self.cycle_end_time - self.cycle_start_time).total_seconds()
