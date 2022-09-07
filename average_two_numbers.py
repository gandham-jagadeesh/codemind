	#average of two numbers
'''
average = sum / count

'''
data=[int(i) for i in input().split()]
sum=data[0]+data[1]  #adding first number + second number
count=len(data)      #taking count 
average=sum/count   #formula for caluclating the average
print('%.4f' %average) #use %f format to print values of float in precison of 4
