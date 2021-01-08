# https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient/problem

N = int(input())
x = [float(n) for n in input().strip().split(' ')]
y = [float(m) for m in input().split(' ')]

def rank_data_set(arr):
    sorted_arr = sorted(arr)
    rank_dict = {num: rank for rank, num in enumerate(sorted_arr)}
    ranks = []
    
    for num in arr:
        ranks.append(rank_dict[num])
        
    return ranks
        
def get_rank_corr_coef(X, Y):
    # first step: rank both data sets
    x_ranks = rank_data_set(X)
    y_ranks = rank_data_set(Y)
    
    # second: get diff in ranks
    d = [xi - yi for (xi, yi) in zip(x_ranks, y_ranks)]
    
    # get sum of the square of the diffs
    d_sq_sum = sum([di**2 for di in d])
    
    # get corr coeff
    ans = 1 - (6 * d_sq_sum / N / (N**2 - 1))
    
    return round(ans, 3)

print(get_rank_corr_coef(x, y))