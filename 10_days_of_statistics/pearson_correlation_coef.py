# https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient/problem

import math

n = int(input())
try:
    x = []
    for n in input().split(' '):
        x.append(float(n))
except ValueError:
    pass

y = list(map(float, input().split(' ')))
        
def get_mean_stdev(arr):
    mean = sum(arr) / len(arr)
    variance = sum([(x-mean)**2 for x in arr]) / len(arr)
    stdev = math.sqrt(variance)
    
    return (mean, stdev)

def get_corr_coef(arr1, arr2, stats1, stats2):
    mu1 = stats1[0]
    sigma1 = stats1[1]
    
    mu2 = stats2[0]
    sigma2 = stats2[1]
    
    numerator = sum([(x - mu1)*(y - mu2) for x, y in zip(arr1, arr2)])
    denominator = len(arr1) * sigma1 * sigma2
    
    corr = numerator / denominator
    
    return round(corr, 3)

print(get_corr_coef(x, y, get_mean_stdev(x), get_mean_stdev(y)))    
