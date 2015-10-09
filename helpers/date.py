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


def days_to_seconds(delta_days):
    """ Given a period in days, convert to seconds."""
    return delta_days * 24 * 60 * 60


def seconds_to_days(delta_seconds):
    """Given a period in seconds, convert to a number of days.
    e.g. seconds_to_days(12 * 60 * 60) --> 0.5
    """
    return float(delta_seconds) / (60 *  60 * 24)