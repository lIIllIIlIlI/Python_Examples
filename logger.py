# Debugger option als Parameter einfügen und debug level definieren


import logger

# Multiple logger in a given script: 
# loggerA = logging.getLogger(__name__ + '.A')
# loggerB = logging.getLogger(__name__ + '.B')

# create logging variables
logFormatter = logging.Formatter(fmt=' %(name)s :: %(levelname)s :: %(message)s')
loggerName = Path(__file__).stem
logFile = loggerName + ".log"
logFilePath = Path(__file__).parent / logFile

# create logger
logger = logging.getLogger(loggerName)
logger.setLevel(logging.DEBUG)

# create console handler
consoleHandler = logging.StreamHandler()
if(verbose):
        consoleHandler.setLevel(logging.DEBUG)
else:
        consoleHandler.setLevel(logging.INFO)
consoleHandler.setFormatter(logFormatter)

# Add console handler to logger
logger.addHandler(consoleHandler)

# install logfile
logFileHandler = logging.FileHandler(logFilePath, mode = 'w')
logFileHandler.setLevel(logging.DEBUG)
logFileHandler.setFormatter(logFormatter)
logger.addHandler(logFileHandler)

# Test
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

      
      
