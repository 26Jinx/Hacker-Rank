# https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem

from math import exp, factorial

avg = float(input())
k = int(input())

def get_poisson_p(rate, desired):
    prob = (rate**desired)*exp(-rate)/factorial(desired)
    
    return prob

print(round(get_poisson_p(avg, k), 3))