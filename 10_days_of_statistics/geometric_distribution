# https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem

fraction = list(map(int, input().split(' ')))
n = int(input())

probability_of_defect = fraction[0]/fraction[1]

# P(k) = (1-p)^(k-1)*p GEOMETRIC DISTRIBUTION
probability_of_defect_at_trial_n = (1-probability_of_defect)**(n-1)*probability_of_defect

print(round(probability_of_defect_at_trial_n, 3))

# alternate solution using function
frac = [int(s) for s in input().split(' ')]
n = int(input())
prob = frac[0]/frac[1]

def geo_dist(probability, occurrence):
    ans = (1-probability)**(occurrence-1)*probability
    
    return ans

print(round(geo_dist(prob, n), 3))