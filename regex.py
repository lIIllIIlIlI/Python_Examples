******* Notes:
- Playground: https://regex101.com/  (Change regex to python!!)
- special characters have to be escaped, including the escape symbol. Example: '[' is catched by \[, '\' is catched by '\\'
- Optional word: (regex)?                                                                                                  
- Naming a group: (?P<name>regex)
- Noncapturing group: (?:regex)    
- not \xy --> \XY                                                                                              
- Hex Pattern = r'0x[0-9a-fA-F]'
     
         
                                                                                                   
******* Basic Examples:                                                                                                   
# Catch regex anywhere in line
if re.search(pattern, line):
  myMatch = re.search(pattern, line).group(0)                                                                                                   

# Catch regex from start of line
if re.match(regex, line):
  myMatch = re.match(regex, line).group(0)                                                                                                   

# substitute
myString = myString.replace("e", "")                                                                                                    
                                                                                                   
# substitute via regex
string = re.sub(regex, replacement, string)
                                                                                                   
         
                                                                                                   
******* Advanced Examples:                                                                                                   
# find all occurences of the regex at a time
fileString = read(...)                                                                                                   
pattern = r'regex'
reObjOfPattern = re.compile(pattern, re.MULTILINE)                                                                                                   
matches = reObjOfPattern.findall(fileString)                                                                                                 
                                                                                                   

                                                                                                                                                                                                                                                                                                     
******* Special Examples:
# Python cant help but interpret backslashes, which causes problem when replaceing something with a path.
# Solution: Convert \ to \\ 
# Note: \ needs to be escaped
backslashedFilePath = re.sub(r'\\', r'\\\\', backslashedFilePath, 0, re.DOTALL)

                                                                                                   


.   matches any character
\d 	digit
\s 	whitespace: [ \t\n\r\f\v]
\w 	alphanumeric: [0-9a-zA-Z_]
\d 	digit
\s 	whitespace: [ \t\n\r\f\v]

^ 	matches beginning of string
$ 	matches end of string

[5b-d] 	  matches any chars '5', 'b', 'c' or 'd'
[^a-c6] 	matches any char except 'a', 'b', 'c' or '6'
[a|b]     matches either a or b

* 	0 or more 
+ 	1 or more 

{m} 	exactly mm occurrences
{m, n} 	from m to n. m defaults to 0, n to infinity
{m, n}? 	from m to n, as few as possible                                                                         

                                                                                               
                                                                                                  
