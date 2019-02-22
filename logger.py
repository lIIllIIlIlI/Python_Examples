# Debugger option als Parameter einfügen und debug level definieren


import logger

resultLogPath = os.path.join(logPath, 'Results.log')
bobLogPath = os.path.join(logPath, 'Bob.log')

resultFormatter = logging.Formatter(fmt='%(asctime)s :: %(levelname)s :: %(message)s', datefmt = '%Y-%m-%d,%H:%M:%S')
resultLogger = setupLogger('resultLogger', 'Results.log', logPath, resultFormatter, logging.INFO, True, 'a')

bobFormatter = logging.Formatter('%(message)s')
bobLogger = setupLogger('bobLogger', 'Bob.log', logPath, bobFormatter, logging.INFO, True, 'a')

# Create or refresh logfiles
open(resultLogPath, "w+")
open(bobLogPath, "w+")

class RainbowLoggingHandler(ColorizingStreamHandler):
    """ 
    A colorful logging handler optimized for terminal debugging aestetichs.
    """

    # Define color for message payload
    level_map = {
        logging.DEBUG: (None, 'cyan', False),
        logging.INFO: (None, 'white', False),
        logging.WARNING: (None, 'yellow', True),
        logging.ERROR: (None, 'red', True),
        logging.CRITICAL: ('red', 'white', True),
    }

    date_format = "%H:%m:%S"

    #: How many characters reserve to function name logging
    who_padding = 22

    #: Show logger name
    show_name = True

    def get_color(self, fg=None, bg=None, bold=False):
        """
        Construct a terminal color code

        :param fg: Symbolic name of foreground color

        :param bg: Symbolic name of background color

        :param bold: Brightness bit
        """
        params = []
        if bg in self.color_map:
            params.append(str(self.color_map[bg] + 40))
        if fg in self.color_map:
            params.append(str(self.color_map[fg] + 30))
        if bold:
            params.append('1')

        color_code = ''.join((self.csi, ';'.join(params), 'm'))

        return color_code

    def colorize(self, record):
        """
        Get a special format string with ASCII color codes.
        """

        # Dynamic message color based on logging level
        if record.levelno in self.level_map:
            fg, bg, bold = self.level_map[record.levelno]
        else:
            # Defaults
            bg = None
            fg = "white"
            bold = False

        template = [
            "[",
            self.get_color("black", None, True),
            "%(asctime)s",
            self.reset,
            "] ",
            self.get_color("white", None, True) if self.show_name else "",
            "%(name)s " if self.show_name else "",
            "%(padded_who)s",
            self.reset,
            " ",
            self.get_color(bg, fg, bold),
            "%(message)s",
            self.reset,
        ]

        format = "".join(template)

        who = [self.get_color("green"),
               getattr(record, "funcName", ""),
               "()",
               self.get_color("black", None, True),
               ":",
               self.get_color("cyan"),
               str(getattr(record, "lineno", 0))]

        who = "".join(who)

        # We need to calculate padding length manualy
        # as color codes mess up string length based calcs
        unformatted_who = getattr(record, "funcName", "") + "()" + \
            ":" + str(getattr(record, "lineno", 0))

        if len(unformatted_who) < self.who_padding:
            spaces = " " * (self.who_padding - len(unformatted_who))
        else:
            spaces = ""

        record.padded_who = who + spaces

        formatter = logging.Formatter(format, self.date_format)
        self.colorize_traceback(formatter, record)
        output = formatter.format(record)
        # Clean cache so the color codes of traceback don't leak to other formatters
        record.ext_text = None
        return output

    def colorize_traceback(self, formatter, record):
        """
        Turn traceback text to red.
        """
        if record.exc_info:
            # Cache the traceback text to avoid converting it multiple times
            # (it's constant anyway)
            record.exc_text = "".join([
                self.get_color("red"),
                formatter.formatException(record.exc_info),
                self.reset,
            ])

    def format(self, record):
        """
        Formats a record for output.

        Takes a custom formatting path on a terminal.
        """
        if self.is_tty:
            message = self.colorize(record)
        else:
            message = logging.StreamHandler.format(self, record)

        return message

#TODO: Alle Filter in einen Filter zusammenfassen
class debugFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == 10
    
class infoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == 20
    
class warningFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == 30

class errorFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == 40

class cricitalFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == 50

      
     
def setupLogger(name, logFile, logPath, formatter, level, stdStream, mode):
    """
    Initializes and returns logger object with logfile and stderr/stdout handler.
    Formatter defines the logging format, namely which data is stored during each 
    logging process.
    Level defines which kind of logging information is safed by the logger. 
    Possible values are 'info' < 'warning' < 'error' < 'critical', all logs on or above level
    are forwarded.
    """
    # Create handles for both file logging and stdout/stderr logging
    logger = logging.getLogger(name)
    logFilePath = os.path.join(logPath, logFile)
    handler = logging.FileHandler(logFilePath, mode)        
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    if(stdStream):
        
        #TODO: StreamHandlerCreator() implementieren
        streamerDebug = RainbowLoggingHandler(sys.stdout)
        streamerDebug.setFormatter(formatter)
        streamerDebug.addFilter(debugFilter())
        logger.addHandler(streamerDebug)
        
        streamerInfo = RainbowLoggingHandler(sys.stdout)
        streamerInfo.setFormatter(formatter)
        streamerInfo.addFilter(infoFilter())
        logger.addHandler(streamerInfo)
        
        streamerWarning = RainbowLoggingHandler(sys.stdout)
        streamerWarning.setFormatter(formatter)
        streamerWarning.addFilter(warningFilter())
        logger.addHandler(streamerWarning)
        
        streamerError = logging.StreamHandler()        
        streamerError.setFormatter(formatter)
        streamerError.addFilter(errorFilter())
        logger.addHandler(streamerError)
        
        streamerCritical = logging.StreamHandler()        
        streamerCritical.setFormatter(formatter)
        streamerCritical.addFilter(cricitalFilter())
        logger.addHandler(streamerCritical)

    logger.setLevel(level)
    return logger

Hauptskript:      
     logfile = ARGUMENTS.get("loggerfile", None)

runFormatter = logging.Formatter('%(message)s')
runLogger = setupLogger('runLogger', logfile, logPath, runFormatter, logging.INFO, True, 'a')

resultFormatter = logging.Formatter(fmt='%(asctime)s :: %(levelname)s :: %(message)s', datefmt = '%Y-%m-%d,%H:%M:%S')
resultLogger = setupLogger('resultLogger', 'Results.log', logPath, resultFormatter, logging.INFO, True, 'a')

bobFormatter = logging.Formatter('%(message)s')
bobLogger = setupLogger('bobLogger', 'Bob.log', logPath, bobFormatter, logging.INFO, True, 'a')

Unterskript:
  runLogger = logging.getLogger('runLogger')
resultLogger = logging.getLogger('resultLogger')
bobLogger = logging.getLogger('bobLogger')



      
      
