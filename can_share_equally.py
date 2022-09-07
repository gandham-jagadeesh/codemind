data=[int(i) for i in input().split()]
if data[0] ==0 and data[1] %2==0:
 print('YES')
elif data[0] ==0 and data[1] %2!=0:
 print('NO')
elif (data[0]+data[1]*2 )%2==0:
 print('YES')
else:
 print('NO')
