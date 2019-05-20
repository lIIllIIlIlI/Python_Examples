# Python tries to resolve \[0-9] and might destroy windows path. Can be prevented by escaping the symbol.
# Even path librarys will not resolve this problem on their own!
wrongPath = 'C:\user\03sourcecode'
rightPath = 'C:\user\\03sourcecode'
print(wrongPath)
print(rightPath)


###########################################################################################################

