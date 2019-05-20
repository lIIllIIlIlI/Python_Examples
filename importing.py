1. Import gesamte Library, keine Namespace übernahme. Elemente der Library müssen durch expliziten Namespace wechsel angesprochen
werden.

import library
usage: library.function()

2. Falls 1 mit Aliasing.

import library as lib
usage: lib.function()

2. Import Library mit Namespace. Die aufgeführten Elemente werden in den Namespace übernommen. Die Benutzung einer Wildcard kann 
daher zu ungewollten Seiteneffekten führen. 

from library import function
usage: function()



