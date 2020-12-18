# https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem

import math

mean, stdev = tuple(map(int, input().split(' ')))
score1 = int(input())
score2 = int(input())

def getCumulativeNormalDistributionFunc(score, mu, sigma):
    error = math.erf((score - mu)/(sigma * math.sqrt(2)))
    ans = (1 + error)/2
    return ans

print(round((1 - getCumulativeNormalDistributionFunc(score1, mean, stdev))*100, 2))
print(round((1 - getCumulativeNormalDistributionFunc(score2, mean, stdev))*100, 2))
print(round((getCumulativeNormalDistributionFunc(score2, mean, stdev))*100, 2))