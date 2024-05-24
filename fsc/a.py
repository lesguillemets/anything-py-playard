import numpy as np
import matplotlib.pyplot as plt
import math

mu = 0.00
sigma = 200
N = 100000
M = 2000
def main():
    rng = np.random.default_rng()
    twologlambdas = np.fromiter( (trial(rng, mu, sigma, N) for _ in range(M)), dtype=float)
    h,b = np.histogram(twologlambdas, bins=100)
    plt.stairs(h,b)
    plt.show()
    print(np.mean(twologlambdas))



def trial(rng, mu, sigma2,n):
    sample = rng.normal(mu, math.sqrt(sigma2), n)
    sample_mean = np.mean(sample)
    sample_var = np.var(sample)
    if False:
        print(f"μhat = {sample_mean}, σ2hat = {sample_var}")
    l0 = sum(  (xi*xi for xi in sample)  )
    l1 = sum( ( (xi-sample_mean)*(xi-sample_mean) for xi in sample ) )
    return n * math.log( l0/l1 )

def norm_sample(rng, mu, sigma2, n):
    return rng.normal(mu, math.sqrt(sigma2), n)

if __name__ == "__main__":
    main()
