from pathlib import Path
import os
import shutil

# print current root path
rootPath = Path.cwd()
print("rootPath: {}".format(rootPath))

# Root path is determined by the caller location, while the script normally expects it's own location. Therefore change root Path
# At the beginning of root python script. Since a script can be called as a library or as root, a if __name__ == '__main__' check
# if required first. All scripts from here have the successor root path and can be handled by relative pathes. 
os.chdir(Path(__file__).parent)

# The actual root path
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
print("The most top level part of the path:  {}".format(scriptDir.name))
print("The name of the top level part without extension: {}".format(scriptDir.stem)
print("The extension of the top level part: {}".format(scriptDir.suffix)
print("The first part of the path:  {}".format(scriptDir.anchor))
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
      
# Creating directory
if not scriptDir.is_dir():
   os.makedirs(scriptDir)
      
# Deleting directory recursively
if scriptDir.is_dir():
   shutil.rmtree(scriptDir, ignore_errors=True)
   # ignore_errors will even delete read only files, basically everything in the folder
      
# Deleting specific file
os.remove(file)
