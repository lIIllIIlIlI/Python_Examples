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



# NAMESPACES/SCOPES
#	
# Variables are passed via pointers on default
#
# direct assignment of objects will create a reference/pointer pair and add it to both objects. To recreate another 
# Object with sama data, deepcopy is used.
#
# "if __name__ == "__main__":" has the same scope as any other code part that is not within functions/classes 
#
# Everything that is not within functions/classes is global by default, setting it global has no effect
#
# Functions/classes don't inherit global variables, they have to be imported by the keyword global.
#
# 
#
#
#
#
#
