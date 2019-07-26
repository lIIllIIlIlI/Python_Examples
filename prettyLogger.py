import logging
from sys import exit
from os import makedirs
from pathlib import Path
from enum import Enum

class LOGMODUS(Enum):
    VERBOSE = 0
    NORMAL = 1
    QUIET = 2

class FILELOGGING(Enum):
    INACTIVE = 0
    ACTIVE = 1

# logfile path, feel free to change
logPath = Path(__file__).parent / "Log"
print(logPath)

if not logPath.is_dir():
    makedirs(logPath)

def getPrettyLogger(loggerName, LOGMODUS, FILELOGGING):
    """
    Creates and returns a logger object

    Input:
        LoggerName: str

        LOGMODUS: enum
            Verbose - full output + full meta data
            normal - normal output + minimal meta data
            quiet - only crucial output + minimal meta data

        FILELOGGING: enum
            active - print to console + logfile
            inactive - print to console only 
    """
    # create logger
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)

    # HANDLER ----------------------------------------------------------------------------------------------
    # create console handler
    consoleHandler = logging.StreamHandler()
    if(LOGMODUS == LOGMODUS.VERBOSE):
        consoleHandler.setLevel(logging.DEBUG)
    elif(LOGMODUS == LOGMODUS.QUIET):
        consoleHandler.setLevel(logging.WARNING)
    elif(LOGMODUS == LOGMODUS.NORMAL):
        consoleHandler.setLevel(logging.INFO)
    else:
        print("Invalid logger mode selected. Please choose from {verbose, quiet, normal}. Exiting ...")
        exit(1)   

    # create logfile handler
    if FILELOGGING == FILELOGGING.ACTIVE:
        logFileName = str(loggerName) + ".log"
        logFilePath = str(logPath / Path(logFileName))
        print("logFilePath: {}".format(logFilePath))
        logFileHandler = logging.FileHandler(logFilePath, mode = 'w')
        logFileHandler.setLevel(logging.DEBUG)

    # set console handler
    logger.addHandler(consoleHandler)

    # set logfile handler 
    if FILELOGGING == FILELOGGING.ACTIVE:
        logger.addHandler(logFileHandler)
    # -------------------------------------------------------------------------------------------------------
    
     # FORMATTER ---------------------------------------------------------------------------------------------
    # create console formatter
    if(LOGMODUS == LOGMODUS.VERBOSE):
        consoleLogFormatter = logging.Formatter(fmt='%(levelname)-6s :: %(filename)-8s :: %(funcName)-15s :: %(lineno)d :: %(message)s')
    else:
        consoleLogFormatter = logging.Formatter(fmt='%(levelname)-6s :: %(message)s')

    # create logfile formatter
    logFileFormatter = logging.Formatter(fmt='%(levelname)-6s :: %(filename)-8s :: %(funcName)-15s :: %(lineno)d :: %(message)s')

    # set console formatter  
    consoleHandler.setFormatter(consoleLogFormatter)        
    
    # Set logfile formatter
    if FILELOGGING:
        logFileHandler.setFormatter(logFileFormatter)
    # ------------------------------------------------------------------------------------------------------
    
    return logger
