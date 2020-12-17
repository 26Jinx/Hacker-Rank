# https://www.hackerrank.com/challenges/s10-normal-distribution-1/problem

import math

mean, stdev = (int(x) for x in input().split(' '))
x_1 = float(input())
x_2, x_3 = (float(y) for y in input().split(' '))

# normal (Gaussian) distribution
# f(x) = sqrt(1/(2πσ^2)) * e^((-x-μ)^2 / 2σ^2)
def get_normal_distribution(mu, sigma, x):
    error_func = math.erf((x-mu) / (sigma*(math.sqrt(2))))
    ans = 1/2 * (1 + error_func)
    return ans

# get prob with given inputs
ans_1 = get_normal_distribution(mean, stdev, x_1)
ans_2 = get_normal_distribution(mean, stdev, x_3) - get_normal_distribution(mean, stdev, x_2)

print(round(ans_1, 3))
print(round(ans_2, 3))