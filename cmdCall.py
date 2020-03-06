from subprocess import Popen
from subprocess import PIPE
from subprocess import STDOUT

command = ["gcc", "-v"]
try:
    # universal_newlines - encodes stream, recommended for text parsing
    process = Popen(command, bufsize=1, universal_newlines=True, stdout=PIPE, stderr=STDOUT)

    if process.returncode:
        print("Cmd was spawned successfully, yet an error occuring during the execution of the command")

    # ---- combined output ----
    # communicate() can only be assigned once
    fullOutput = process.communicate()
    print("Full output: {}\n\n".format(fullOutput))

    # ---- separated output ----
    stdout, stderr = process.communicate()
    print("Normal output: {}", stdout)
    print("Error output: {}", stderr)

    # ---- greedy output ----
    for line in iter(process.stdout.readline, ''):
        print(line)

    # ---- some processes wont terminate but keep printing black lines ----
    lineCounter = 0
    prevLine = ''
    for line in iter(process.stdout.readline, ''):
        print(line)
         if line == prevLine:
             lineCounter += 1
             if lineCounter > 50:
             break
     else:
         prevLine = line
         lineCounter = 0

except Exception as exceptionError:
    print("Command {} can't be started. Error message: {}".format(command, exceptionError))
