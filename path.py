# Wird ein Skript aus der ferne aufgerufen bzw innerhalb einer Ide über eine Ordnerstruktur hinweg, ist nicht klar welches library
# welchen Pfad als root bezeichnet, den Pfad der Aufrufers oder den Pfad des Skriptes. Daher sollte der Skriptpfad absolut zur 
# Lautzeit eingeholt werden und alle weiteren Pfade von dort aus relativ bestimmt werden. 

from pathlib import Path
import os

# Tricky, because script might be called from somewhere other than script path.
# Path(__file__).parent is more stable
scriptDir = Path.cwd()
print("Script directory (Path.cwd()): {}". format(scriptDir))

logDir = scriptDir / "Logfile" / "mylogfil.log"
print("logDir: {}".format(logDir))

# Alternativ
logDirParts = ["Logfile", "mylogfile.log"]
logDir = scriptDir.joinpath(*logDirParts)
print("logDir created by joining a list: {}".format(logDir))

# pathlib erstellt path objekte, keine strings. Möchte man einen String zu einem Path Objekt machen oder umgekehrt geht dies wie folgt: 
dirString = Path(scriptDir) erstellt ein Path Objekt aus einem String
print("Type of dirString after generation a pathlib object: {}".format(type(dirString)))
dirString = str(dirString)
print("Type of dirString after converting to string: {}".format(type(dirString)))
      
print("Is the script dir a directory? {}".format(scriptDir.is_dir()))
print("Or is it a file? {}".format(scriptDir.is_file()))
print("If it wasn't already, abs path could be created: {}".format(scriptDir.absolute()))
print("Note parts, anchor and parent are member variables of object 'Path' and not functions!")
print("Anyway, it consists of the following parts: {}".format(scriptDir.parts))
print("The most top level part of the path:  {}".format(scriptDir.anchor))
print("Parent of the path: {}".format(scriptDir.parent))
print("Parent of the parent: {}".format(scriptDir.parent.parent))
relPath = "../../test"
print("When mixing absolut with relative path, remember to resolve the path: {}".format((scriptDir / relPath).resolve())

# Alle Ordner und Datein im Ordner listen:
for element in scriptDir.glob('*.*'):
    print("Name of found elements (Membervariable of Path obj): {}".format(element.name))

# Rekursiv
for element in scriptDir.rglob('*.*'):
    print("Name of found elements (Membervariable of Path obj): {}".format(element.name))
