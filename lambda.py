# Creates a one line function in place, e.g. to pass it down another function

# Example1:
# Basic example how lambda works
x = lambda a : a + 10
print(x(5)) 

# Does the same as:
def x(a):
  return a + 10

print(x(5))

# Example 2: 
# Sort a list of class objects by member variable "address".
# The sorted function gets a custom function handle instead of picking a default one
class myClass():
    def __init__(self, address):
        self.address = address

unsortedList = [myClass("0xAB"), myClass("0x10"), myClass("0xab"), myClass("0x01"), myClass("0xBA")]
sortedList = sorted(unsortedList, key=lambda element: int(element.address, 16))

print([element.address for element in unsortedList])
print([element.address for element in sortedList])
