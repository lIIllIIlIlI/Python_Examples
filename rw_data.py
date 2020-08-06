from pathlib import Path
import shutil


myFile = Path(Path.cwd() / "myFile") 

if myFile.is_file():
    pathlib.Path.unlink(myFile)

# create or append
with myFile.open('a+') as fileDeskriptor:
    dump(self, fileDeskriptor, HIGHEST_PROTOCOL)
  
# create or overwrite
with myFile.open('w+') as fileDeskriptor:
    dump(self, fileDeskriptor, HIGHEST_PROTOCOL)
    
# read file to variable with try/catch
if myFile.is_file():
    with myFile.open("r", encoding='utf-8', errors="ignore") as fileDeskriptor:
        myFileContent = fileDeskriptor.readlines()
else:
    print("Could not find {} during enum extraction".format(myFilee))
    
        
