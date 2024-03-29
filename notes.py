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


###########################################################################################################

# Integrationsprozess:
#
#	1. Bestehenden Code sortieren und modular abtrennen in eine Blackbox und einen Integrationsteil
#	2. Von der Blackbox sowie dem Integrationsteil Architektur vom IST-Zustand erstellen
#	3. Von der Blackbox, dem Integrationsteil sowie der Erweiterung Architektur vom SOLL-Zustand erstellen. Dabei sehr 
#	   kleinschrittig vorgehen und ein gesamtes Datenmodell abbilden.
#	4. Falls benötigt Blackbox Driver erstellen, der alle späteren Betriebszustände genau abbildet.
# 	5. Blackbox Test erstellen
#	6. Separierten Teil Implementieren und mit Blackbox driver testen. Während dem Implementieren Architektur
#	   falls nötig aktualisieren.
#	7. Integration & Integrationstests


# include modules in different folders:
# 1. case: module is deeper than root:
#
#	1. Solution: 'import deeperfolder.mymodule'
#	2. Solution: create empty __init__.py in deeperfolder and 'from deepfolder import mymodule'. 
#
# 2. case: module is somewhere else:
#	1. Add mymodule to sys path:  'sys.path.insert(0, r'../../my/module/folder')'
#	2. 'import mymodule'
#


# Bei der List comprehension treten bisher unbekannte Seiteneffekte auf:
variablesTypedefs = ([variable.name for variable in bswAsap2Vars]) verändert bswAsap2Vars
# TODO: Beispiele aufstellen und das Verhalten nachvollziehen

# Sort list of dictionaries/objects by value:
# Make sure the key value is int, not str!
import operator
myDictObjectList.sort(key = operator.itemgetter('age'))

# get object with certain value of a key:
male_subset_gen = filter(lambda x: x.sex == 'm', people_set)


*args, **kws: args are skalars, kws are dict items.

# Create an object list from uniform yaml file
with open('employees.yaml') as f:
        employees = [Employee(**empl) for empl in yaml.safe_load(f)]

# Convert fomula into integer
formulaString = "((2u) + ((4u) + (4u) + (4u) ) + (((2u) + (4u) ) * (16u)))"
formulaStringCleaned = re.sub("[u|U]", "", formulaString)
integer = eval(formulaStringCleaned)

# Ensure certain python version
assert sys.version_info >= (3, 5)

# Add path to import other python modules from  different projects. This is quite a dirty hack, the project should contain
# all required skripts. Helper modules should be deposited in default python pathes. Configs should be stored in a config files 
# and not be included as a module
sys.path.insert(0, r'relative/path/myPython.py')
import myPython


# if you are uncertain if a dictionary exists, check it before accessing it
if myDict and key in myDict:
    print("found key")

# Try/except blocks prevent keyboard interrupts, having bigger code parts within those blocks is bad practice.

# Underscores:
class Test():
	def __init__():
		# public variable, access for everyone
		self.a = 0 
		# protected, access for class and subclasses
		# protection has to be manually implemented via setter/getter
		self._b = 1
		# private, access for class only
		# python protects c by renaming it internally to _<class_name>__c, preventing accidental access
		self.__c = 2
	def a():
		"""
		Accessible from everywhere
		"""
		return
	def _b():
		"""
		Accessible by class and subclasses
		"""
		return
	def __c():
		"""
		Accessible by class only
		"""
		return
# Unautorized variable access in a threat to objects, but not to functions.
# If someone has a deep wish to access your local module functions, it doesnt 
# need to bother you. Therefore, mark them with a single underscore and rely
# on the user for some common sense. 
