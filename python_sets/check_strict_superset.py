# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

set_a = set(map(int, input().split(' ')))
n = int(input())

for i in range(n):
    subset = set(map(int, input().split(' ')))
    ans = True
    
    if set_a > subset:
        continue
    else:
        ans = False
        break
        
print(ans)