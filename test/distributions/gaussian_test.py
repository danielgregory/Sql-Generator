__author__ = 'Daniel Gregory'

import unittest
from math import sqrt
from datetime import datetime
from helpers.date import convert_datetime_to_seconds, seconds_to_days, days_to_seconds
from distributions.gaussian import gaussian_generator, gaussian_date_generator


class TestGaussianDistributions(unittest.TestCase):
    """ Confirms that we get a Gaussian distribution."""
    def test_gaussian_generator(self):
        """ Tests that a Gaussian distribution of numbers has the correct mean
        and standard deviation."""
        expected_mean = 10
        expected_sigma = 15
        gg = gaussian_generator(expected_mean, expected_sigma)
        for _ in range(10):
            distribution = [next(gg) for _ in range(10000)]
            actual_mean = self.mean(distribution)
            actual_sigma = self.standard_deviation(distribution)

            # assert that the mean is about 10
            self.assertGreater(actual_mean, 9.6)
            self.assertLess(actual_mean, 10.4)

            # assert that the standard deviation
            # is around 15
            self.assertGreater(actual_sigma, 14.5)
            self.assertLess(actual_sigma, 15.5)

    def test_gaussian_date_generator(self):
        """ Confirm that the generated dates are distributed according
        to a Gaussian. We doe this assertion 10 times.
        """
        expected_mean = datetime(2014, 6, 1)
        expected_sigma_in_days = 100
        gg = gaussian_date_generator(expected_mean, expected_sigma_in_days)
        for _ in range(10):
            distribution = [next(gg) for _ in range(100000)]
            seconds = [convert_datetime_to_seconds(d) for d in distribution]
            actual_mean = self.mean(seconds)
            diff = actual_mean - convert_datetime_to_seconds(expected_mean)
            diff_in_days = seconds_to_days(diff)
            one_day = 1

            # assert stuff
            self.assertLessEqual(diff_in_days, one_day)

            actual_sigma = self.standard_deviation(seconds)
            diff = abs(actual_sigma - days_to_seconds(expected_sigma_in_days))
            self.assertLessEqual(diff, days_to_seconds(1))

    def mean(self, distribution):
        """ Helper function. Given a distribution, calculate the mean."""
        return float(sum(distribution)) / len(distribution)

    def standard_deviation(self, distribution):
        """ Helper function. Given a distribution, calculate the standard
        deviation (sigma)."""
        count = len(distribution)
        mean = self.mean(distribution)
        diff_squared = 0
        for x in distribution:
            diff_squared = diff_squared + (x - mean) ** 2
        variance = float(diff_squared) / count
        return sqrt(variance)