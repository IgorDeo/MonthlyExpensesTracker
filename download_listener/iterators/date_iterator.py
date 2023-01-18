from dateutil.rrule import rrule, MONTHLY
from datetime import datetime
from .iterator import Iterator


class DateIterator(Iterator):
    def __init__(
        self,
        from_date: datetime = None,
        to_date: datetime = None,
        file_extension: str = None,
    ):
        if not from_date or not to_date or not file_extension:
            raise ValueError("from_date, to_date and file_extension are required")
        self.from_date = from_date
        self.current = from_date
        self.current_str = self.current.strftime("%m%Y")
        self.end = to_date
        self.file_extension = file_extension
        self.months = rrule(MONTHLY, dtstart=self.current, until=self.end)
        self.months_iter = iter(self.months)

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if self.current >= self.end:
            raise StopIteration
        self.current = self.months_iter.__next__()
        self.current_str = f'{self.current.strftime("%m%Y")}.{self.file_extension}'
        return self.current_str

    def reset(self):
        self.current = self.from_date
        self.current_str = f'{self.current.strftime("%m%Y")}.{self.file_extension}'
        self.months = rrule(MONTHLY, dtstart=self.current, until=self.end)
        self.months_iter = iter(self.months)
        self.months_iter.__next__()
