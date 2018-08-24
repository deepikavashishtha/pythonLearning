def readfile(fileName):
	try:
		f = open(fileName, "r")
		myList = []
		for line in f:
			myList.append(line)
		print(myList)
		f.close()
	except Exception:
        	print("cant read the file")
	return

def main():
	fileName = raw_input("enter filename you like to read:")
	print(fileName)	
	readfile(fileName)
	

main()
