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

logger.info("*** Initialise input arguments: SUCCESS ***")
logger.info("*** Initialise logger: SUCCESS ***")
                    
###################################################################################################
#                                Init Logger                                                      #
###################################################################################################

# create logger
loggerName = Path(__file__).stem
logFormatter = logging.Formatter(fmt=' %(name)s :: %(levelname)s :: %(message)s')
logger = logging.getLogger(loggerName)
logger.setLevel(logging.DEBUG)

# create console handler
Handler = logging.StreamHandler()
if(args.verbose):
        Handler.setLevel(logging.DEBUG)
else:
        Handler.setLevel(logging.INFO)
Handler.setFormatter(logFormatter)

# Add console handler to logger
logger.addHandler(Handler)

# install logfile
logFileHandler = logging.FileHandler(logFilePath, mode = 'w')
logFileHandler.setLevel(logging.DEBUG)
logFileHandler.setFormatter(logFormatter)
logger.addHandler(logFileHandler)
                    
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

