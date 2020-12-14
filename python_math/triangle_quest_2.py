# https://www.hackerrank.com/challenges/triangle-quest-2/problem

# rules of the exercise dictated that I could not use more than one line
# and could not use anything related to strings

# my attempt
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(int((10**(i-1) if i > 0 else 0) + (10**(i-2) if i > 1 else 0) + (10**(i-3) if i > 2 else 0) + (10**(i-4) if i > 3 else 0) + (10**(i-5) if i > 4 else 0) + (10**(i-6) if i > 5 else 0) + (10**(i-7) if i > 6 else 0) + (10**(i-8) if i > 7 else 0) + (10**(i-9) if i > 8 else 0))**2)

# more neat solution
# print((10^(i-1)//9)**2)