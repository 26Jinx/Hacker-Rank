# https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

import math

# Complete the countTriplets function below.
def countTriplets(arr, r):
    triplets = 0

    if r == 1:
      triplets = math.factorial(len(arr))/int(math.factorial(3)*math.factorial(len(arr) - 3))
      return int(triplets)
    else:
      num_dict = {}
      for i, n in enumerate(arr):
          if n in num_dict:
              num_dict[n].append(i)
          else:
              num_dict[n] = [i]
      print(num_dict)

    for k, v in num_dict.items():
      trps_keys = [k*r**i for i in range(3)]
      print(trps_keys)

      if any(val not in num_dict for val in trps_keys):
        break
      else:
        this_trip = 1
        for n in trps_keys:
          this_trip *= len(num_dict[n])
        triplets += this_trip 
          
    return triplets