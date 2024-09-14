#THIS IS A MICROPYTHON FILE
import math
def calculate_mean_variance(pmf):
    """
    Calculate the mean and variance from a given PMF.

    Parameters:
    pmf (dict): A dictionary where keys are the values of the random variable
                and values are the probabilities associated with those values.

    Returns:
    tuple: A tuple containing the mean and variance.
    """
    mean = 0
    mean_squared = 0

    for x, p in pmf.items():
        mean += x * p
        mean_squared += (x ** 2) * p

    variance = mean_squared - (mean ** 2)

    return mean, variance

def uniform_variance(a, b):
        "Parameters: a, b are the bounds of the uniform distribution"
    numerator = (b-a + 1)**2 - 1
    denominator = 12 
    return numerator / denominator

def uniform_mean(a, b):
    "Parameters: a, b are the bounds of the uniform distribution"
    return (a + b) / 2



def binomial_mean(n, p):
    return n*p

def binomial_std_dev(n, p):
    return math.sq

