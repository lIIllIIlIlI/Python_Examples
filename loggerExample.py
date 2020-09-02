# TODO: Create an example project with multiple Modules as well as a CONF and a LOG folder. Create a config for a logger and store it in
# CONFIG with a file logger to LOG/logger.log. In the main function, register the root logger and simply call the logger in all child 
# modules.
# rel: https://stackoverflow.com/questions/15727420/using-logging-in-multiple-modules (not the accepted answer, dont be lazy, scroll!)

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
