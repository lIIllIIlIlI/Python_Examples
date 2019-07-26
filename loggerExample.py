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
