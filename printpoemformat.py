def readfile(fileName):
	f = open(fileName, "r")
	myList = []
	for line in f:
		myList.append(line)
	print(myList, 3*3)
	f.close()
	return

def main():
	fileName = raw_input("enter filename you like to read:")
	print(fileName)	
	readfile(fileName)
	

main()
