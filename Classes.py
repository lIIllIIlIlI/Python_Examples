class A:
  """
  some random class
  """
  def __init__(self, name, myString):
    self.name = name
    self.myString = myString
    self.anotherVar = 5
    
#   def __repr__(self):
#     """
#     There is a implicit default __repr__ that prints "self.__class__.__name__, id(self)". This defines what is returned 
#     when print is called on the function. To create a pretty printing, this can be explicitely overriden.
#     """
#     return "<class: %s\n name:%s,\n myString:%s,\n anotherVar:%d>" % \
#          (self.__class__.__name__, \
#           self.name, self.myString, \
#               self.anotherVar)

  def __repr__(self):
    """
    There is a implicit default __repr__ that prints "self.__class__.__name__, id(self)". This defines what is returned 
    when print is called on the function. To create a pretty printing, this can be explicitely overriden.
    __repr__ should give some information about the object to developer.
    """
    returnString = ""
    returnString += "<class: " + self.__class__.__name__ + ",\n"
    returnString += " name: " + str(self.name) + ",\n"
    returnString += " myString: " + str(self.myString) + ",\n"
    returnString += " anotherVar: " + str(self.anotherVar) + ">\n"
    return returnString
    
  def __str__(self):
      """
      This one should give the user a quick feedback.
      """
      return "Im here"

myObject = A("greeting", "hello world") 
print(myObject)
