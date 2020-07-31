import subprocess
import re
from pathlib import Path
import sys

# NOTES ############################################################################################
# text=True will convert the output to ASCII to avoid the trailing b'' annotation
#
# text is an alias for universal_newlines
#
# subprocess.check_output is depracated, it causes three different bugs:
#       1. Successfull operation returns error code
#       2. Operation with error code does not return a string
#       3. Failed operation kills the python execution, try/catch required
#
# Subprocess executes the command internally and ignores PATH. If elements in Path are required, pass
# shell = True
#
# The function communicate() return the whole thing while process.stdout holds small buffers. Therefore
# communication() might kill windows or be killed by windows for buffer oberflows. Therefore, avoid the
# function. 
#
# communication() can be called only once
#
# subprocess.run is the recommended approach yet it lacks configuration parameters. Run will call
# Popen internally, it's an abstraction layer for run to make the call simpler and handle details.
#
# The subprocess.run call manages the execution and returns a CompleteProcess object once it's executed.
# Therefore, no explicit synchonisation is necessary. Futhermore, the user has to take care that the 
# execution acutally finishes, for example by parsing the greedy output for repetetive lines.
# Furthermore, the user has to take care that the process is actually killed once all output is received.
#
# Currently, the only reasonable scanario to use Popen instead of run is to greedy print
#
# To capture stdin/stderr in the right order, the stderr stream needs to be piped to stdout. Having
# both streams separaetly an still printing the proper order does not work.  
#
# run takes an optional timeout parameter and will raise a timeout once the tasks did not terminate within
# the given time. 
#
# A lot of tools will intentionally print to stderr instead of stdout to get printed by calling programs,
# e.g. gcc.
#
#
#######################################################################################################

def runCommand(command):
    """
    Runs the given command via subprocess and returns the output which consists of both 
    the stdout and stderr stream. 

    Input: command list
        command to be executed
    
    Output: output list
        List of stderr and stdout lines that the command cmd call generated
    """
    output = []
    process = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.STDOUT, \
                         text = True, shell = True)
    if process.returncode:
        errorMessage = "".join([line for line in process.stderr])
        print("Command {} returned with error status {}. The process reported the \
following errors:\n{}".format(command, process.returncode, errorMessage))
    for line in process.stdout:
        output.append(line.rstrip())
    return output

# EXAMPLE0
output = runCommand(["gcc", "-v"])


print("\n")
print('*** EXAMPLE1: Grep version from "gcc -v" output that prints everything to stderr ***')
gccVersion = None
gccVersionRegex = r'gcc version (?P<version>\d+\.\d+\.\d+)'
command = ['gcc', '-v']
outputRegex = r'gcc version (?P<version>\d+\.\d+\.\d+)'
process = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.STDOUT, \
                         text = True, shell = True)
# stdout contains both stdout and stderr
if process.stdout is not None:
    for line in process.stdout:
        if re.search(gccVersionRegex, line):
            gccVersion = re.search(gccVersionRegex, line).group("version")
if process.returncode:
    errorMessage = "".join([line for line in process.stderr])
    print("Command {} returned with error status {}. The process reported the \
following errors:\n{}".format(command, process.returncode, errorMessage))
if gccVersion is None:
    print("Warning: Could not receive the gcc version")
else:
    print("Extracted gcc version: {}".format(gccVersion))
print("\n")


print('*** EXAMPLE2: run svn info, print warnings only ***')
command = ['svn', 'info', 'C:\\Projects\\SW26.01']
process = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.PIPE, \
                         text = True, shell = True)
if process.stdout is not None:
    for line in process.stdout:
        print(line.rstrip())
if process.returncode:
    errorMessage = "".join([line for line in process.stderr])
    print("Command {} returned with error status {}. The process reported the \
following errors:\n{}".format(command, process.returncode, errorMessage))
elif process.stderr is not None:
    warningMessages = "".join([line for line in process.stderr])
    print(warningMessages)
print("\n")


print('*** EXAMPLE3: Greedy print output (direct Popen call) ***')
try:
    command = ["size", "-v"]
    # bufsize creates a line buffer for stdout/err
    process = subprocess.Popen(command, bufsize=1, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print("The following print is executed while the process is still runing")
    for line in iter(process.stdout.readline, ''):  
        print(line.rstrip())
except Exception as exceptionMessage:
    print("Execution of the command {} returned the following error: {}".format(command, exceptionMessage))
process.wait()
print("The code behind the print (e.g. returncode check) will be executed no matter if the execution finished! Sync manually!")
if process.returncode:
    print("The execution of the command {} returnes the error code {}.".format(command, process.returncode))
print("The command wait will stop the execution until the process terminates. If the read get aborted, e.g. because the data got \n\
extracted successfully, the process is still running and might cause a windows buffer overflow. Therefore, make sure to terminate \n\
the process.")
# process.terminate()







