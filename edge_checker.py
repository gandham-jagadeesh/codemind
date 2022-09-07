data=[int(i) for i in input().split()] #reading using list comphresion
data.sort()
if data[0] == 1 and data[1] == 10:
 print('Yes')
elif data[0]+1 == data[1]:
 print('Yes')
else:
 print('No')
