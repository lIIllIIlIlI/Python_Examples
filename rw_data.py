from pathlib import Path


myFile = Path(Path.cwd() / "myFile.txt") 

if myFile.is_file():
    Path.unlink(myFile)

# create or overwrite
with myFile.open('w+') as fileDeskriptor:
    fileDeskriptor.write("Hello\n")

# create or append
with myFile.open('a+') as fileDeskriptor:
    fileDeskriptor.write("World!")
    
# read file to variable with try/catch
if myFile.is_file():
    with myFile.open("r") as fileDeskriptor:
        myFileContent = fileDeskriptor.readlines()
        for line in myFileContent:
            print(line)
else:
    print("Could not find {} during enum extraction".format(myFilee))
    
        
