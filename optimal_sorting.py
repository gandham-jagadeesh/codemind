#optimal sorting
def solve(length,lists):
 count=0
 max_value=max(lists)
 max_list=lists.index(max_value) == (length-1)
 for i in range(0,length-1):
  if lists[i] < lists[i+1]:
   count=count+1
 if count == length-1:
  print(0)
 elif max_list:
  min_value=min(lists)
  operation=max_value-min_value
  print(operation)
  print(1)
test_case=int(input())
for i in range(test_case):
 length=int(input())
 lists=[int(i) for i in input().split()]
 solve(length,lists)

#this week -> solve these problems one problem every day
