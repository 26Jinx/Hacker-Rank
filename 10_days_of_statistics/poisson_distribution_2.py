# https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem

rates = [float(x) for x in input().split(' ')]

# the expected occurrences with the avg rate of a is E[X]=a + a^2
print(160 + 40 * (rates[0] + rates[0]**2))
print(128 + 40 * (rates[1] + rates[1]**2))