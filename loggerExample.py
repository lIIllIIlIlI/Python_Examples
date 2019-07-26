from prettyLogger import getPrettyLogger
from prettyLogger import logModus
from prettyLogger import fileLogging

# Debug logger
print("\n\n")
print("****   debug logger   ****")
print("\n\n")
debugLogger = getPrettyLogger("exampleLogger", logModus.VERBOSE, fileLogging.ACTIVE)

debugLogger.debug("Hello")
debugLogger.info("Pierburg,")
debugLogger.warning("I")
debugLogger.critical("am")
debugLogger.error("Logger")

# normal logger
print("\n\n")
print("****   normal logger   ****")
print("\n\n")
normalLogger = getPrettyLogger("normalLogger", logModus.NORMAL, fileLogging.ACTIVE)

normalLogger.debug("Hello")
normalLogger.info("Pierburg,")
normalLogger.warning("I")
normalLogger.critical("am")
normalLogger.error("Logger")

# quiet logger
print("\n\n")
print("****   quiet logger   ****")
print("\n\n")
quietLogger = getPrettyLogger("quietLogger", logModus.QUIET, fileLogging.ACTIVE)

quietLogger.debug("Hello")
quietLogger.info("Pierburg,")
quietLogger.warning("I")
quietLogger.critical("am")
quietLogger.error("Logger")
