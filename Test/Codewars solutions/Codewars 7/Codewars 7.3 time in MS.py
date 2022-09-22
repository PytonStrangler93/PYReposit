# Clock shows h hours, m minutes and s seconds after midnight.
# Your task is to write a function which returns the time since midnight in milliseconds.
# Example:
#h = 0
#m = 1
#s = 1
#result = 61000
# Input constraints:
#0 <= h <= 23
#0 <= m <= 59
#0 <= s <= 59

import datetime
from datetime import timedelta


def past(h, m, s):
    # Good Luck!
    h = h * 60 * 60 * 1000
    m = m * 60 * 1000
    s = s * 1000

    return (h + m + s)


def past(h, m, s):
    return timedelta(hours=h, minutes=m,
                     seconds=s) // timedelta(milliseconds=1)


def past(h, m, s):
    dt = datetime.timedelta(hours=h, minutes=m, seconds=s)
    return 1000 * dt.total_seconds()
