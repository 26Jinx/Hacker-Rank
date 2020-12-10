# https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem

conditions = input().split(' ')

rej_rate = float(conditions[0])/100
sample_size = int(conditions[1])

def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result

def get_prob(sample, desired, rate):
    result = factorial(sample)/factorial(desired)/factorial(sample-desired)*(rate**desired)*((1-rate)**(sample-desired))
    
    return result

# now we need to calculate the combined probablities of at most 2 being rejected
# i.e. P(2) + P(1) + P(0)
max_desired = get_prob(sample_size, 2, rej_rate) + get_prob(sample_size, 1, rej_rate) + get_prob(sample_size, 0, rej_rate)

print(round(max_desired, 3))

# the probability of at least 2 being rejected is equal to 1 - 'max_desired' plus
# P(2)
min_desired = get_prob(sample_size, 2, rej_rate) + (1 - max_desired)

print(round(min_desired, 3))