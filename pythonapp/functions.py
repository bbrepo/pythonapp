#FUNCTION

#Create a function
def sayHello(name='Bidhan'):
    'Print hello to name'
    print('Hello',name)
    
sayHello('Brad')

#Return a value
def getSum(num1,num2):
    total=num1+num2
    return total

numSum=(1, 2)
print(numSum)

#Mutable and nonmutable

def addOneToNum(num):
    num=num+1
    print('Value inside function:' ,num)
    return

num=5
addOneToNum(num)
print('Value outside function:' ,num)

def addOneToList(myList):
    myList.append(4)
    print('Value inside function: ' , myList)
    return 
myList=[1,2,3]
addOneToList(myList)
print('Value outside function: ', myList)


    