# Playground: https://pythex.org/
\ 	escape special characters
. 	matches any character
^ 	matches beginning of string
$ 	matches end of string
[5b-d] 	matches any chars '5', 'b', 'c' or 'd'
[^a-c6] 	matches any char except 'a', 'b', 'c' or '6'
R|S 	matches either regex R or regex S
() 	creates a capture group and indicates precedence

* 	0 or more (append ? for non-greedy)
+ 	1 or more (append ? for non-greedy)
? 	0 or 1 (append ? for non-greedy)
{m} 	exactly mm occurrences
{m, n} 	from m to n. m defaults to 0, n to infinity
{m, n}? 	from m to n, as few as possible

\A 	start of string
\b 	matches empty string at word boundary (between \w and \W)
\B 	matches empty string not at word boundary
\d 	digit
\D 	non-digit
\s 	whitespace: [ \t\n\r\f\v]
\S 	non-whitespace
\w 	alphanumeric: [0-9a-zA-Z_]
\W 	non-alphanumeric
\Z 	end of string
\g<id> 	matches a previously defined group

(?iLmsux) 	matches empty string, sets re.X flags
(?:...) 	non-capturing version of regular parentheses
(?P...) 	matches whatever matched previously named group
(?P=) 	digit
(?#...) 	a comment; ignored
(?=...) 	lookahead assertion: matches without consuming
(?!...) 	negative lookahead assertion
(?<=...) 	lookbehind assertion: matches if preceded
(?<!...) 	negative lookbehind assertion
(?(id)yes|no) 	match 'yes' if group 'id' matched, else 'no'

regexString = re.search(r'customRegex', string)

Examples:
command: rfrString = re.search(r'RAM_FROM_RUN[ ]*PROGBITS[ ]*\d*[ ]\d*[ ]*\d*',str(stdout))
Output: Extrahiert RAM_FROM_RUN    PROGBITS   000032   000043   000054 aus dem String heraus
Nachbearbeitung: rfrElements = rfrString.group(0).split()
                 rfrStringValue = rfrElements[-1]
 
 re.search liefert ein Objekt zurück, möchte man die entsprechenden Elemente als Liste zurück bekommen ist die Funktion re.findall
 zu verwenden. Mit  einem len(rückgabewert) lässt sich die Anzahl an treffern ermitteln. 
 
 Testen der Regex:
 https://regex101.com/r/g0E3qB/1

