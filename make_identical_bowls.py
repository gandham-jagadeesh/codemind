length=int(input())
array=[int(i) for i in input().split()]
maximum=[]
temp=0
for i in range(len(array)):
 temp=temp+array[i]
for i in range(1,length+1):
  if temp%i==0:
   maximum.append(i)
print(max(maximum))
