def helloworld(mystring):
	print(mystring)
	myName = raw_input("what is your name?")
	myvar = raw_input("enter a number?")
	print(myName)
	print(myvar)
	if(myName == "abc" and myvar == 0):
		print("correct name")
	elif(myName == "elis" or myvar == 1):
		print("good name")
	else:
		print("you are ok")

helloworld("hello python")
