index=int(input())
test_cases=[int(i) for i in input().split()]
index=int(input())
test_cases=[int(i) for i in input().split()]
element=test_cases[0]
count=1
max_element=max(test_cases)
index_last=(test_cases.index(max_element)==(index-1))
for i in range(1,len(test_cases)):
    if element == test_cases[i]:
        count=count+1
if count == index:
    print(0)
elif index_last:
    print(1)
else:
    print(2)
'''
how do i know that reversing helps
how do i know when to make elements equal
how to check all the elements are equal
'''
