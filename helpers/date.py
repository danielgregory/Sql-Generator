__author__ = 'Daniel Gregory'
 # TODO: remainder look at this next
 # TODO: formats dates correctly ...

import datetime


def convert_datetime_to_seconds(dt):
    """
    Gets the total number of seconds since 01/01/1970.
    See: http://stackoverflow.com/questions/6999726/how-can-i-convert-a-datetime-object-to-milliseconds-since-epoch-unix-time-in-p
    """
    start = datetime.datetime.utcfromtimestamp(0)
    delta = dt - start
    return delta.total_seconds()

