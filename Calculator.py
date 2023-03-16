class calculator:
    #Class Atribut

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def add (self): #Method penambahan
        return self.number1 + self.number2
    
    def substract (self): # Method pengurangan
        return self.number1 - self.number2
    
    def multiply(self): # Method perkalian
        return self.number1 * self.number2
    
    def divide (self): # Method Pembagian
        if self.number2 == 0:
            return 'Error'
        else:
            return self.number1 / self.number2
    

print ('Choose Operation')
print ('1. Add')
print ('2. Substract')
print ('3. Multiply')
print ('4. Divide')

Choice = input ('Choose only number 1/2/3/4: ') # input operasi yang ingin dipilih
number1 = float(input('Input number 1: '))
number2 = float(input('Input number 2: '))

calculator = calculator (number1, number2) #pembuatan objek calculator

if Choice == '1':
    print(number1, ' + ', number2, ' = ', calculator.add())

elif Choice == '2':
    print (number1, ' - ', number2, ' = ', calculator.substract())

elif Choice == '3':
    print (number1, ' * ', number2, ' = ', calculator.multiply())

elif Choice == '4':
    print (number1, ' / ', number2, ' = '. calculator.divide())

else:
    print('Invalid number')
