#This module allows operations with arrays, lists and tuples
def searchNum(list, number):
	"""
	Search numbers in arrays, lists or tuples. 				
        Returns number and index (number,index)
	"""
	index = 0
	for i in list:
		index += 1
		if i == number:
			return i, index - 1
		else:
			pass

def searchWord(list, word):
	"""
	Searchs words in arrays, lists or tuples.
	Returns word and index (word, index)
	Literally, does the same as searchNum
	"""
	index = 0
	for i in list:
		index += 1
		if i == word:
			return i, index - 1
		else:
			pass
			
def arrSave(file, array):
	"""
	Saves arrays, lists or tuples in a text file
	"""
	try:
		f = open(file, "a")
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

def addArray(arr1, arr2):
	"""
	Adds the values of the first array, list or tuple to the second and returns a new array, list or tuple
	(The arrays must be equal size)
	"""
	newarr = []
	for i in range(len(arr1)):
		newarr.append(arr1[i] + arr2[i])
	return newarr

def subsArray(arr1, arr2):
	"""
	Same as addArray, but substracts values
	"""
	newarr = []
	for i in range(len(arr1)):
		newarr.append(arr1[i] - arr2[i])
	return newarr
	
def multArray(arr1,arr2):
	"""
	Same as addArray, but multiplicates values
	"""
	newarr=[]
	for i in range(len(arr1)):
		newarr.append(arr1[i] * arr2[i])
	return newarr

def divArray(arr1,arr2):
	"""
	Same as addArray, but divides values
	"""
	newarr=[]
	for i in range(len(arr1)):
		newarr.append(arr1[i] / arr2[i])
	return newarr

def matrixToList(mat):
	"""
	Gets all data from a matrix or bidimensional lists and return it as a regular list
	"""
	new = []
	for i in mat:
		if type(i) == list:
			for k in i:
				new.append(k)
		else:
			new.append(i)
	return new
