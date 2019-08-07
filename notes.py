# Python tries to resolve \[0-9] and might destroy windows path. Can be prevented by escaping the symbol.
# Even path librarys will not resolve this problem on their own!
wrongPath = 'C:\user\03sourcecode'
rightPath = 'C:\user\\03sourcecode'
print(wrongPath)
print(rightPath)
 
###########################################################################################################	

except Exception as exceptionError:
	print("my error handling output. The actual output: {}".format(exceptionError))

###########################################################################################################

# Deleting/Adding items while iterating over data structure:
#    Solution: Iterate over a copy of said data structure
myList = [1, 2, 3, 4, 5]
for number in list(myList):
	if number == 2:
		myList.remove(number)

###########################################################################################################

myList = ["hello", "world"]
for index, elem in enumerate(myList):
	if index == 0:
		print(elem)
	else:
		print(myList[elem])
	

###########################################################################################################
# Read list of value from object list
[typeDef.name for typeDef in typeDefs]
