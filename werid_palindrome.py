def solve(unique,data):
 for i in range(len(data)):
  data[i]=data[i]%2
 garbage=0
 for i in range(len(data)):
  garbage=garbage+data[i]
 value=garbage//2
 print(value)

test_cases=int(input())
for i in range(test_cases):
 unique=int(input())
 data=[int(i) for i in input().split()]
 solve(unique,data)

#https://www.codechef.com/submit/MAKEPAL?tab=statement
