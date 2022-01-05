# Custom exceptions allow other programs to handle the exceptions
#   e.g. if the library code breaks because the passed file does not exist or the host system is windows but the library only works for linux
# They are really usefull when implementing libraries as they perform certain actions for a program in a bigger context
# Standalone programs often dont profit from custom exception as the callee has no good use for the passed information.
# The only situation where it might make sense for standalone programs is to create one exception instead of redundant logging message

# Use built in exceptions for standalone programs
