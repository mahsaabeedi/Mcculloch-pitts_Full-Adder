

x_bit0=input("Enter  bit 0 binary number1 :") 
x_bit1=input("Enter  bit 1 binary number1 :") 
y_bit0=input("Enter  bit 0 binary number2 :") 
y_bit1=input("Enter  bit 1 binary number2 :") 

A0=x_bit0
A1=x_bit1
B0=y_bit0
B1=y_bit1

#X=input("Enter  bit binary number ") 
#y=input("Enter  bit binary number ") 
#
#A0=X[0]
#A1=X[1]
#B0=y[0]
#B1=y[1]

teta=2  
def activationfunc(x):
    if x>=teta:
        x=1
    else:
        x=0
    return x

        
##calculate  sum 0

Z1= 2*int(A0) + (-1)*int(B0)
Z1=activationfunc(Z1)
Z2= 2*int(B0) + (-1)*int(A0)
Z2=activationfunc(Z2)



sum0 = 2*int(Z1) + 2*int(Z2)
sum0=activationfunc(sum0)
print("sum0" , sum0)


    
#calculate sum1
Z3 =2*int(A1) + (-1)*int(B1)
Z3 =activationfunc(Z3)

Z4 =2*int(B1) + (-1)*int(A1)
Z4=activationfunc(Z4)

Z11 = 2*int(Z3) + 2*int(Z4)
Z11 =activationfunc(Z11)

M=int(A0) + int(B0)
M=activationfunc(M)

Z5 =2*int(M) + (-1)*int(Z11)
Z5=activationfunc(Z5)

Z6 =2*int(Z11) +(-1)*int(M)
Z6= activationfunc(Z6)

sum1 = 2*int(Z5) + 2*int(Z6)
sum1= activationfunc(sum1)
print("sum1",sum1) 
#calculate carry 
Z7 =int(A1) + int(B1)    
Z7 =activationfunc(Z7)

Z8 =int(Z11) + int(M)
Z8 =activationfunc(Z8)


Z9 = 2*int(Z8)+(-1)*int(Z7)
Z9 = activationfunc(Z9)

Z10 =2*int(Z7) + (-1)*int(Z8)
Z10 =activationfunc(Z10)

carry = 2*int(Z9) + 2*int(Z10)
carry = activationfunc(carry)
print("carry",carry)


print("sum of the binary number is:" + str(carry) +str(sum1) + str(sum0))