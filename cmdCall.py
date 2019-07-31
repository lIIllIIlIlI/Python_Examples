from subprocess import Popen
from subprocess import PIPE
from subprocess import STDOUT

command = ["gcc", "-v"]
try:
    # universal_newlines - encodes stream, recommended for text parsing
    process = Popen(command, bufsize=1, universal_newlines=True, stdout=PIPE, stderr=STDOUT)

    if process.returncode:
        print("Cmd was spawned successfully, yet an error occuring during the execution of the command")

    # communicate() can only be assigned once
    fullOutput = process.communicate()
    print("Full output: {}\n\n".format(fullOutput))

    # alternative
    # stdout, stderr = process.communicate()
    # print("Normal output: {}", stdout)
    # print("Error output: {}", stderr)

    # alternative
    # Greedy output
    # lineCounter = 0
    # for line in iter(process.stdout.readline, ''):
        # Some process will not terminate but coninuously print blank lines
        # this might be solved with a counter
        # if(lineCounter < 50):
            # print(line)
            # lineCounter += 1

except Exception as exceptionError:
    print("Command {} can't be started. Error message: {}".format(command, exceptionError))
