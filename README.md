# About it

I'm creating this program to automate my montly expenses tracking. Currently i've made an listener that watches a directory for new files and, once downloaded, rename it to the next file name from an iterator. 


### How to use download_listener

```python
from download_listener.download_listener import DownloadListener
import datetime
from download_listener.iterators.date_iterator import DateIterator

from_date = datetime.datetime(2019, 1, 1)
to_date = datetime.datetime(2019, 12, 1)

default_file_name = "Enter your default file name here"
working_dir = "Enter your working directory here"

date_iterator = DateIterator(from_date=from_date, to_date=to_date)
listener = DownloadListener(working_dir=working_dir, files_names_iterator=date_iterator)


listener.listen(default_file_name)
```