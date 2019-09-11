class A:
  """
  some random class
  """
  def __init__(self, name, myString):
    self.name = name
    self.myString = myString
    self.anotherVar = 5
    
  def __repr__(self):
    """
    There is a implicit default __repr__ that prints "self.__class__.__name__, id(self)". This defines what is returned 
    when print is called on the function. To create a pretty printing, this can be explicitely overriden.
    """
    return "<class: %s\n name:%s,\n myString:%s,\n anotherVar:%d>" % (self.__class__.__name__, self.name, self.myString, self.anotherVar)
    
print(A("greeting", "hello world"))
