#add function
def add(num1, num2):
	return num1 + num2

#Minus function
def minus(num1, num2):
	return num1 - num2

#multiply function
def multiply(num1, num2):
	return num1 * num2

#devide function
def divide(num1, num2):
	return num1 / num2

#area function
def area(num1):
	return 3.14 * num1 * num1

def main():
	operation = raw_input("what do you want to do(+,-,*,/,area):")
	if(operation != '+' and operation != '-' and operation != '*' and operation != '/' and operation != 'area'):
		print("invalid operation")
	else:
		var1 = input("enter num1: ")
		var2 = input("enter num2: ")
		if(operation == '+'):
			myval = add(var1, var2)
			print(myval)
		if(operation == '-'):
			myval = minus(var1, var2)
			print(myval)
		if(operation == '*'):
			myval = multiply(var1, var2)
			print(myval)
		if(operation == '/'):
			myval = divide(var1, var2)
			print(myval)
		if(operation == 'area'):
			myval = area(var1)
			print(myval)



main()


