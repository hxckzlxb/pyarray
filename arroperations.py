#This module allows operations with arrays, lists and tuples
def searchNum(list, number):
	"""
	Search numbers in arrays, lists or tuples
	"""
	index = 0
	for i in list:
		index += 1
		if i == number:
			return i, index - 1
		else:
			pass

def arrSave(file, array):
	"""
	Saves arrays, lists or tuples in a text file
	"""
	try:
		f = open(file, "w")
		f.write(str(array))
		f.close()
		print("The array was succesfully saved")
	except:
		print("The array cannot be saved")
		
def arrLoad(file):
	"""
	Loads arrays, lists or tuples from text files
	"""
	try:
		f = open(file, "r")
		arr = f.read()
		print("Array loaded")
		return arr
	except:
		print("Array could not be loaded")