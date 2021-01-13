# https://www.hackerrank.com/challenges/s10-least-square-regression-line/problem

scores = []

for _ in range(5):
    scores.append(list(map(int, input().split(' '))))
   
math_scores = [score[0] for score in scores]
stats_scores = [score[1] for score in scores]

def get_regr_line(lst_X, lst_Y):
    n = len(lst_X)
    sum_x_times_y = sum([x*y for x, y in zip(lst_X, lst_Y)])
    sum_x = sum(lst_X)
    sum_y = sum(lst_Y)
    sum_x_sq = sum([x**2 for x in lst_X])
    
    slope = (n*sum_x_times_y - sum_x*sum_y)/(n*sum_x_sq - sum_x**2)
    
    intercept = (sum_y/n) - slope * (sum_x/n)
    
    return (intercept, slope)
    

# now enter a score into equation and get most likely score for 
# the other test
def get_y(x, intercept, slope):
    y = intercept + slope * x
    return y

intrcpt, slp = get_regr_line(math_scores, stats_scores)

print(round(get_y(80, intrcpt, slp), 3))