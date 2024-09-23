#THIS IS A MICROPYTHON FILE
import math


def uniform_variance(a: float, b:float)-> float:
        "Parameters: a, b are the bounds of the uniform distribution"
        numerator = (b-a + 1)**2 - 1
        denominator = 12 
        return numerator / denominator

def uniform_mean(a, b) -> float:
    "Parameters: a, b are the bounds of the uniform distribution"
    return (a + b) / 2

def binomial_mean(n, p):
    return n*p

def binomial_std_dev(n, p):
    return math.sqrt(n*p*(1-p))

def binomial_variance(n, p):
    return n*p*(1-p)

def standardize(x, mean, std_dev):
    return (x - mean) / std_dev

#if __name__ == "__main__":
#    main()

def main():
    usin = None
    while True:
        print("Welcome to Liam's stat library")
        print("0. Distributions")
        usin = str(input("Choose an option: "))

        match usin:
            case '0':
                break
                # distributions()
def distributions():
    print("Distributions")
    print("0. Uniform")
    print("1. Binomial")
    print("2. Poisson")
    print("3. Geometric")
    print("4. Bernoulli")
    print("99. Go Back")

    usin = str(input("Choose an option: "))
    match usin:
        case '0' :
            uniform_distrib()
        case '1': 
            # binomials()
            print("")
def uniform_distrib():
    print("Uniform Distributions:")
    print("0. Uniform Mean")
    print("1. Uniform Variance")
    # TODO: 
    print("2. Uniform Std Dev")

    usin = str(input("Choose: "))
    match usin: 
        case '0':
            a = float(input("Lower Bound"))
            b = float(input("Upper Bound"))
            print(uniform_mean(a,b))
        
