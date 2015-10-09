__author__ = 'Daniel Gregory'

import matplotlib.pyplot as plt
import datetime
from distributions.gaussian import gaussian_date_generator


def plot_points(points, bins):
    """
    Helps out with plotting histograms
    """
    plt.hist(points, bins)
    plt.show()


def plot_gaussian_dates():
    """
    Used to demonstrate that the Gaussian date generator is indeed a Gaussian.
    This function will display a histogram - it should look bell-shaped!
    """
    # generate test data
    mean = datetime.datetime(2010, 12, 1, 0, 0)
    sigma_in_days = 100
    dates = gaussian_date_generator(mean, sigma_in_days)
    dates_in_seconds = [(dates.next() - datetime.datetime.utcfromtimestamp(0)).total_seconds()
                        for _ in range(1000)]
    plot_points(dates_in_seconds, 100)




