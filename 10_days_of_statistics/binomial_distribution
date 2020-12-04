# https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem

ratio = list(map(float, input().split(' ')))

p = ratio[0]/sum(ratio)
n = 6       # 6 children
k = 3       # 3 boys

def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
        
    return result

def boys_prob(children, boys, p_of_boy):
    prob_of_k = factorial(children) / factorial(boys) / factorial(children-boys) * p_of_boy**(boys) * (1-p_of_boy)**(children-boys)
    
    return prob_of_k

at_least_3_boys = 1 - boys_prob(6, 2, p) - boys_prob(6, 1, p) - boys_prob(6, 0, p)

print(round(at_least_3_boys, 3))