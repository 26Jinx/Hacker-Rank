# https://www.hackerrank.com/challenges/find-angle/problem

import math

y = int(input())
x = int(input())

def get_theta_of(adjacent, opposite, radians=True):
    tan_of_theta = opposite/adjacent
    
    # inverse to get alpha
    theta = math.atan(tan_of_theta)
    
    return (theta if radians else math.degrees(theta))

ans = get_theta_of(x, y, False)

if ans == 0.5:
    ans = math.ceil(ans)
else:
    ans = round(ans, 0)

print(f'{ans:.0f}°')