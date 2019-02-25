import pprint

def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

def advancedPrint(printElement):
   print(namestr(printElement, globals()))
   pprint.pprint(printElement, width=10) 
    
myDict = {"variable": "5",
          "list": [1,2,3,4,5],
          "stringList": ["eins", "zwei", "drei", "vier", "fünf"],
          }

advancedPrint(myDict)
