#calculator assignment

num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))
operation = input("operation being used: ")

if operation == '+':  
    result = num1 + num2  
elif operation == '-':  
    result = num1 - num2  
elif operation == '*':  
    result = num1 * num2  
elif operation == '/':  
    result = num1 / num2  
elif operation == '**':
    result = num1 ** num2
else:  
    result = "Invalid"  

print(result)
