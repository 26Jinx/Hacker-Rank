# https://www.hackerrank.com/challenges/s10-interquartile-range/problem

q = int(input())
entries = list(map(int, input().split(' ')))
freq = list(map(int, input().split(' ')))

# create data set
data_set = []

for i in range(q):
    for _ in range(freq[i]):
        data_set.append(entries[i])

# sort data set array
data_set.sort()

# split the data set in half
def halve(l):
    halfway_i = len(l) // 2
    
    if len(l) % 2 == 0:       #even number of elements
        first_half = l[:halfway_i]
        second_half = l[halfway_i:]
    else:
        first_half = l[:halfway_i]
        second_half = l[halfway_i+1:]
        
    return [first_half, second_half]

def get_median(l):
    first_half = halve(l)[0]
    second_half = halve(l)[1]
    
    if len(l) % 2 == 0:   # even 
        median = (first_half[-1] + second_half[0]) / 2
    else:
        median = l[len(first_half)]
    
    return median

q1 = get_median(halve(data_set)[0])
q3 = get_median(halve(data_set)[1])
    
print(float(q3 - q1))