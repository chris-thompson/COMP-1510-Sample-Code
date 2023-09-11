"""
Here are some neat things we can do with the datetime module.
"""

import datetime
import time


def main():
    """
    Demonstrate datetime module.
    """
    now = datetime.datetime.now()
    print(now)
    print(type(now))

    final_exam = datetime.datetime(2022, 12, 8, 13, 0, 0)
    print(final_exam.year, final_exam.month, final_exam.day, final_exam.hour, final_exam.minute, final_exam.second)
    print(final_exam)

    print(datetime.datetime.fromtimestamp(1000000))
    print(datetime.datetime.fromtimestamp(time.time()))  # need to import time

    christmas = datetime.datetime(2022, 12, 25)
    nyd = datetime.datetime(2023, 1, 1)
    xmas = datetime.datetime(2022, 12, 25)
    print(christmas == xmas)
    print(christmas < nyd)
    print(nyd != xmas)

    delta = datetime.timedelta(days=9, hours=21, minutes=5, seconds=0)
    print(delta.days, delta.seconds, delta.microseconds)
    print(delta.total_seconds())
    print(str(delta))
    print(final_exam.strftime('%Y/%m/%d'))


if __name__ == "__main__":
    main()
