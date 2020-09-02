# TODO: Create an example project with multiple Modules as well as a CONF and a LOG folder. Create a config for a logger and store it in
# CONFIG with a file logger to LOG/logger.log. In the main function, register the root logger and simply call the logger in all child 
# modules.
# rel: https://stackoverflow.com/questions/15727420/using-logging-in-multiple-modules (not the accepted answer, dont be lazy, scroll!)
# Questions left: How to implement libraries? https://docs.python.org/3/howto/logging.html#configuring-logging-for-a-library
# Question left: How to use multiple loggers? Use only one global logger, temporary add yet another file handler and delete is afterwards

# Work steps:
# 1. Create example project https://docs.python.org/3/howto/logging.html#logging-from-multiple-modules
# 2. Create a config 
# 3. Load and test config in main module
# 4. Use and test logger in other modules
# 5. Google, create a forum thread about multiple loggers, play around with temporary adding file handlers
# 6. Read about how to implement logger for libraries
# 7. Insert an error logger that pipes the error/critical message in yet another error.log logfile

# Print detailed infos about the error of a try block
# logger.info("unexpected exception", exc_info=True) 
       
# Print stack information
# logger.info("finished the operation", stack_info=True)

# Logger are always global for a project, the registering is unnecessary. Simply import the config in the main module and a simple
# logger.getLogger(__name__) in the child will do the job. 

# make sure to deactivate other loggers when loading the logger, it's a config parameter

# Always use logger.info("string template %s",argument) to save up computation time

# basicConfig will create a quite good config for the root logger, therefore only has to be called once.

# Loggers support buffers, this could be used to print the last debug info after an error, even if the level is set to info

# Its possible to register custom filters that do stuff every time the logger is called

from prettyLogger import getPrettyLogger
from prettyLogger import LOGMODUS
from prettyLogger import FILELOGGING

# Debug logger
print("\n\n")
print("****   debug logger   ****")
print("\n\n")
debugLogger = getPrettyLogger("exampleLogger", LOGMODUS.VERBOSE, FILELOGGING.ACTIVE)

debugLogger.debug("Hello")
debugLogger.info("Pierburg,")
debugLogger.warning("I")
debugLogger.critical("am")
debugLogger.error("Logger")

# normal logger
print("\n\n")
print("****   normal logger   ****")
print("\n\n")
normalLogger = getPrettyLogger("normalLogger", LOGMODUS.NORMAL, FILELOGGING.ACTIVE)

normalLogger.debug("Hello")
normalLogger.info("Pierburg,")
normalLogger.warning("I")
normalLogger.critical("am")
normalLogger.error("Logger")

# quiet logger
print("\n\n")
print("****   quiet logger   ****")
print("\n\n")
quietLogger = getPrettyLogger("quietLogger", LOGMODUS.QUIET, FILELOGGING.ACTIVE)

quietLogger.debug("Hello")
quietLogger.info("Pierburg,")
quietLogger.warning("I")
quietLogger.critical("am")
quietLogger.error("Logger")
