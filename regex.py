# Playground: https://regex101.com/  (Change regex to python!!)

.   matches any character
\d 	digit
\D 	non-digit
\s 	whitespace: [ \t\n\r\f\v]
\S 	non-whitespace
\w 	alphanumeric: [0-9a-zA-Z_]
\W 	non-alphanumeric
\d 	digit
\D 	non-digit
\s 	whitespace: [ \t\n\r\f\v]
\S 	non-whitespace

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

\w 	alphanumeric: [0-9a-zA-Z_]  // variable name
\W 	non-alphanumeric

Special notes:
- special characters have to be escaped, including the escape symbol. Example: '[' is catched by \[, '\' is catched by '\\'
- Optional word: (regex)?                                                                                                  
- Naming a group: (?P<name>regex)
- Noncapturing group: (?:regex)                                                                                              
  
# line operation                                                                                                 
originalString = "Test string"                                                                                                  
pattern = r'regex'
extractedString = re.match(pattern, originalString)                                                                                                   
                                                                                                   
# find all occurences of the regex at a time
fileString = read(...)                                                                                                   
pattern = r'regex'
reObjOfPattern = re.compile(pattern, re.MULTILINE)                                                                                                   
matches = reObjOfPattern.findall(fileString)
# There are a couple more functions to delete/replace certain elements of string   
                                                                                                   
# Catch regex anywhere in line
re.search(pattern, line)

# Catch regex from start of line
re.search(pattern, line)
myMatch = re.search(pattern, line)                                                                                                   

# substitute     - NOTE: string.replace("old string", "new string) doesn't work for some reason
string = re.sub(r'stringToBeReplaced', "new string", string)

# Python cant help but interpret backslashes, which causes problem when replaceing something with a path.
# Solution: Convert / to // 
# Note: / needs to be escaped
backslashedFilePath = re.sub(r'\\', r'\\\\', backslashedFilePath, 0, re.DOTALL)
                                                                                                   
                                                                                                   
 Hex Pattern = r'0x[0-9a-fA-F]'
                                                                                                   
                                                                                                   
 Testen der Regex:
 https://regex101.com/r/g0E3qB/1
