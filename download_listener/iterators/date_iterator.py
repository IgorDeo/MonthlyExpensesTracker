from dateutil.rrule import rrule, MONTHLY
from datetime import datetime
from .base_iterator import Iterator


class DateIterator(Iterator):
    def __init__(self, from_date: datetime = None, to_date: datetime = None):
        self.current = from_date
        self.current_str = self.current.strftime("%m%Y")
        self.end = to_date
        self.months = rrule(MONTHLY, dtstart=self.current, until=self.end)
        self.months_iter = iter(self.months)

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if self.current >= self.end:
            raise StopIteration
        self.current = self.months_iter.__next__()
        self.current_str = self.current.strftime("%m%Y")
        return self.current_str
