# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from scipy import stats

size = int(input())
lst= list(map(int, input().split())) #split splits numbers into list elements, map casts to int, list makes a list

print(np.mean(lst))
print(np.median(lst))
print(int(stats.mode(lst)[0])) #[0] takes away all the details and keeps [x]
