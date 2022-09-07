length=int(input())
numbers=[int(i) for i in input().split()]
temp=0
for i in range(len(numbers)):
 temp=temp+numbers[i]
if temp%2==0:
 print(1)
else:
 print(0)
'''number=int(input())
values=[int(i) for i in input().split()]
data_even=[]
data_all=[]
for i in range(len(values)):
    for j in range(i+1,len(values)):
        data_all.append(values[i]+values[j])
        if (values[i] + values[j])%2==0:
            data_even.append(values[i]+values[j])
if len(data_even) == len(data_all):
    print(1)
else:
    print(0)
'''
