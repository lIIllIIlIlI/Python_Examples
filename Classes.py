class A:
  """
  some random class
  """
  def __init__(self, name, myString):
    self.name = name
    self.myString = myString
    self.anotherVar = 5

  def __str__(self):
    """
    This one should give the user a quick feedback
    """
    objectDescriptionString = "\n"
    objectDescriptionString += " name: " + str(self.name) + ",\n"
    objectDescriptionString += " myString: " + str(self.myString) + ",\n"
    objectDescriptionString += " anotherVar: " + str(self.anotherVar) + ">\n"
    return objectDescriptionString
    
  def __repr__(self):
      """
      There is a implicit default __repr__ that prints "self.__class__.__name__, id(self)". This defines what is returned 
      when print is called on the function. To create a pretty printing, this can be explicitely overriden.
      __repr__ should give some information about the object to developer.
      """
      objectDescriptionString = "\n"
      objectDescriptionString += "<class: " + self.__class__.__name__ + ",\n"
      objectDescriptionString += " name: " + str(self.name) + ",\n"
      return objectDescriptionString
      
myObject = A("greeting", "hello world") 
print(myObject)
