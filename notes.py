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

Attached/Remote debugging:

1. Install module ptvsd
2. Insert following lines in code:
	import ptvsd
	# 5678 is the default attach port in the VS Code debug configurations
	ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True)
	ptvsd.wait_for_attach()
3. Create Attach debug configuration with vsc:
	{
            "name":"Python: Attach",
            "type":"python",
            "request":"attach",
            "port":5678,
            "host":"localhost",
            "pathMappings":[{
                "localRoot":"C:\\Projects\\3PP_A2l\\04_SwBuild\\BuildTools\\Bob",
                "remoteRoot":".",
                            }]
        },
	
	
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
#	2. Solution: create empty __init__.py in deeperfolder and 'import mymodule'. 
#
# 2. case: module is somewhere else:
#	1. Add mymodule to sys path:  'sys.path.insert(0, r'../../my/module/folder')'
#	2. 'import mymodule'
#


# Bei der List comprehension treten bisher unbekannte Seiteneffekte auf:
variablesTypedefs = ([variable.name for variable in bswAsap2Vars]) verändert bswAsap2Vars
# TODO: Beispiele aufstellen und das Verhalten nachvollziehen
