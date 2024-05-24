import numpy as np
import matplotlib.pyplot as plt
import math

a = 1000
n = 3
trials = 40000

def main():
    rng = np.random.default_rng()
    results = [ single_trial(rng) for _ in range(trials) ]
    h,b = np.histogram(results, bins=a+1)
    mean = np.mean(results)
    print(f"mean = {mean}")
    plt.stairs( list(map(lambda n: n / trials,h)),b)
    plt.plot( [f(x,a) for x in range(a+1)] )
    plt.show()


def f(x,a):
    return 3 * (a-x)*(a-x) / (a*a*a)

def single_trial(rng):
    xs = (rng.uniform(0, a) for _ in range(n))
    x1 = min(xs)
    return x1



if __name__ == "__main__":
    main()
