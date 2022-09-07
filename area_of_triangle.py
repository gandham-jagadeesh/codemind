values=[int(i) for i in input().split()]
a=values[0]
b=values[1]
c=values[2]
s = (a + b + c) / 2
# calculate the area  
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
print('%0.2f' %area)
