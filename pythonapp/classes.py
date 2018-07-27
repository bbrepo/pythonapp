#Classes and Object

# Create class
class Person:
    __name=' ' 
    __email=' '

#Constructor
    def __init__(self,name,email):
        self.__name=name
        self.__email=email

#Getters and Setters        
    def set_name(self,name):
        self.__name=name
        
    def get_name(self):
        return self.__name
    
    def set_email(self,email):
        self.__email=email
        
    def get_email(self):
        return self.__email

#Function
    def toString(self):
        return '{} can be contacted at {} '.format(self.__name,self.__email)
     
#Instantiate the object
#bidhan=Person('Bidhan Biswas', 'bidhanbiswas.cse@gmail.com')

#bidhan.set_name('Bidhan Biswas')
#bidhan.set_email('bidhanbiswas.cse@gmail.com')

#print(bidhan.get_name())
#print(bidhan.get_email())
#print(bidhan.toString())

#Inheritance
class Customer(Person):
    __balance=0
    
    def __init__(self, name, email, balance):
        self.__name=name
        self.__email=email
        self.__balance=balance
        super(Customer,self).__init__(name, email)
    
    def setBalance(self, balance):
        self.__balance=balance
        
    def getBalance(self):
        return self.__balance
    
    def toString(self):
        return '{} has a balance {} and can be contacted at {} '.format(self.__name,self.__balance, self.__email)  
    
john= Customer ('John','John@gmail.com',100) 

john.setBalance(400)
print(john.toString())


     