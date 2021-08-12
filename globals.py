# Some facts:
# - a module variable is global by default, adding a 'global <variable>' doesnt do anything
# - on default, module variables are readable within a function. However write access to the variable will create a local variable with the same name
# - Init variables via 'global <variable> to make the module variable read/writable within the modul

global a # statement has no effect
a = 0
b = 1

def printer():
  global b
  print(a)
  print(b)
  a = -1
  b = -1
  print("a and b set to -1 by printer")
  
printer() # prints a = 0, b = 1
printer() # prints a = 0, b = -1 as b was written by printer


# Reasons not to use globals:
  # 1. Race conditions/mutex waiting time for parallel execution
  # 2. Side effects which affects debugging, testing and reading. A function should always generate the same results when called with the same parameters. Having
  #    a global variable alternating the function execution is obiously bad for a couple of reasons. This gets worses once the project hits a decent size.
  # 3. Importing the module might change the functions behaviour which affects other modules who already imported it. 
  
# Scenarios where they are usefull and are not effected by the reasons above:
  # 1. Constants, a 'MODULE_VERSION = 1.0' is fine
  
  
# What to do instead of global variables:



