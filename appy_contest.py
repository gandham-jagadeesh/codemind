import math
def lcm(a, b):
    return abs(a*b)
def solve(array):
 number=array[0]
 a=array[1]
 b=array[2]
 min_=array[3]
 no_div_a=number/a
 no_div_b=number/b
 no_div_both_a_b=number/lcm(a,b)
 value=no_div_a+no_div_b+2*no_div_both_a_b
 if value >= min_:
  print('Win')
 else:
  print('Lose')
test_case=int(input())
for i in range(test_case):
 array=[int(i) for i in input().split()]
 solve(array)
