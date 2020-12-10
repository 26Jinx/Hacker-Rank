# https://www.hackerrank.com/challenges/polar-coordinates/problem

import re
import cmath

input_str = input()
coef = re.findall(r'-?\d+', input_str)
comp_n = complex(int(coef[0]), int(coef[1]))

print(abs(comp_n))
print(cmath.phase(comp_n))