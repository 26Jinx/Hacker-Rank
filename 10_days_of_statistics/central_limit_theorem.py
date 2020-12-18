# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/problemimport math

import math

max_w = int(input())
n = int(input())
mean = int(input())
stdev = int(input())

# find the probability that the elevator can transport all 49 boxes
# that is to say, what is the probability that the total weight of the 49 boxes
# is less than the max weight allowed?

def getNormalDistributionProb(x, n, mu, sigma):
    # central limit theorem says: N(mu', sigma') where mu' = mu * n and 
    # sigma' = sigma * sqrt(n)
    mu_prime = mu * n
    sigma_prime = sigma * math.sqrt(n)
    
    error_f = math.erf((x - mu_prime)/(sigma_prime * math.sqrt(2)))
    prob = (1 + error_f) / 2
    
    return prob

print(round(getNormalDistributionProb(max_w, n, mean, stdev), 4))