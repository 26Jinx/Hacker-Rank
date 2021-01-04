# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3/problem

n = int(input())
pop_mean = int(input())
pop_stdev = int(input())
coverage = float(input())
z = float(input())

# since z-score is (x - μ)/σ but since we want the bounds for 
# a sample, we need to use σ' = σ/sqrt(n)
b = z * (pop_stdev)/(n**(1/2)) + pop_mean
a = -z * (pop_stdev)/(n**(1/2)) + pop_mean
print(a)
print(b)