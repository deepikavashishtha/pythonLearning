def readfile(fileName):
	f = open(fileName, "r")
	myList = []
	for line in f:
		myList.append(line)
	print(myList)
	f.close()
	return

def main():
	fileName = raw_input("enter filename you like to read:")
	print(fileName)	
	readfile(fileName)
	

main()
