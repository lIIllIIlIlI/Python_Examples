###################################################################################################
#                                Description                                                      #
#    This is a short module description                                                           #
#                                                                                                 #
#    Author:                                                                                      #
#                                                                                                 #
#    Contact:                                                                                     #   
#                                                                                                 #
###################################################################################################


###################################################################################################
#                                Imports                                                          #
###################################################################################################
import logging
import sys
import argparse

from pathlib import Path

###################################################################################################
#                                Input Arguments                                                  #
###################################################################################################
parser = argparse.ArgumentParser()

# optional 
parser.add_argument('--clean','-c', help = 'clean build folder before compilation', action="store_true", default=False)
# choices, required
parser.add_argument('--instrumentation','-i', help = 'List of instrumentations, multiple instrumentations allowed. Example: --instrumentation Xcp Profiler', choices = build_instrumentations, nargs = '+', required = True)
# integer 
parser.add_argument('--nocores', '-n', help='Number of vCores available in the system is default.', type = int, required = False)
# custom string
parser.add_argument('--path...)

args = parser.parse_args()

print(args.nocores)

###################################################################################################
#                                Init Logger                                                      #
###################################################################################################
logger = logging.getLogger(__name__)
# loggerA = logging.getLogger(__name__ + '.A')
# loggerB = logging.getLogger(__name__ + '.B')

logFilePath = Path.cwd() / __name__ + ".log"
handler = logging.FileHandler(logFilePath, 'info')

                    
###################################################################################################
#                                Global Variables                                                 #
###################################################################################################

###################################################################################################
#                                Functions                                                        # 
###################################################################################################

def init():
    """
    The init functions performs a couple of initialization and checks.
    """
    # Check if Python >= 3.5 is installed
    if sys.version_info < (3, 5, 0):
        sys.stderr.write("You need Python 3.5 or greater to run this script \n")
        exit(1)
        
    
    
    
    
if __name__ == '__main__':
    init()

