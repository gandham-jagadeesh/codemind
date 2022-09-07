length=int(input())
test_case=[int(i) for i in input().split()]
for i in test_case:
 if i%2 !=0:
  count=count+1
if count >2:
 print('YES')
 else:
  print('NO')
