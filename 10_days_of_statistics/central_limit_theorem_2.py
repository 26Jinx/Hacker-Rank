# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-2/problem

import math

tix = int(input())
studs = int(input())
mean = float(input())
stdev = float(input())

def get_ndist_prob(n, x, mu, sigma):
    mu_prime = n * mu
    sigma_prime = math.sqrt(n) * sigma
    
    error_f = math.erf((x - mu_prime)/(sigma_prime * math.sqrt(2)))
    prob = (1 + error_f) / 2
    
    return prob

print(round(get_ndist_prob(studs, tix, mean, stdev), 4))