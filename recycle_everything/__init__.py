import logging


ONE_MILLIMETER = 1
ONE_CENTIMETER = ONE_MILLIMETER*10
ONE_DECIMETER = ONE_CENTIMETER*10
ONE_METER = ONE_CENTIMETER*10
ONE_CUBIC_CENTIMETER = ONE_CENTIMETER ** 3
ONE_CUBIC_DECIMETER = ONE_DECIMETER ** 3
ONE_CUBIC_METER = ONE_METER ** 3


class BaseRecycleEverythingError(Exception):
    pass

class InvalidValue(BaseRecycleEverythingError):
    pass


class Area:
    def __init__(self, width_mm: int, length_mm: int):
        if width_mm < 0 or length_mm < 0:
            raise InvalidValue(f'Area dimensions must be positive. Received: {width_mm}, {length_mm}')
        self.width_mm = width_mm
        self.length_mm = length_mm

    def __str__(self) -> str:
        return f'{self.width_mm}mm x {self.length_mm}mm'


class Dimensions:
    def __init__(self, width_mm: int, length_mm: int, height_mm: int):
        if width_mm < 0 or length_mm < 0 or height_mm < 0:
            raise InvalidValue(f'Dimensions must be positive. Received: {width_mm}, {length_mm}, {height_mm}')
        self.width_mm = width_mm
        self.length_mm = length_mm
        self.height_mm = height_mm

    def __str__(self) -> str:
        return f'{self.width_mm}mm x {self.length_mm}mm x {self.height_mm}mm'

    def volume(self) -> int:
        return self.width_mm * self.length_mm * self.height_mm


ONE_CUBIC_CENTIMETER = Dimensions(ONE_CENTIMETER, ONE_CENTIMETER, ONE_CENTIMETER)
ONE_CUBIC_METER = Dimensions(ONE_METER, ONE_METER, ONE_METER)


class ColorLogFormatter(logging.Formatter):
    '''
    Custom formatter that changes the color of logs based on the log level.
    '''

    grey = "\x1b[38;20m"
    green = "\u001b[32m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    blue = "\u001b[34m"
    cyan = "\u001b[36m"
    reset = "\x1b[0m"

    timestamp = '%(asctime)s - '
    loglevel = '%(levelname)s'
    message = ' - %(message)s'

    FORMATS = {
        logging.DEBUG:    timestamp + blue + loglevel + reset + message,
        logging.INFO:     timestamp + green + loglevel + reset + message,
        logging.WARNING:  timestamp + yellow + loglevel + reset + message,
        logging.ERROR:    timestamp + red + loglevel + reset + message,
        logging.CRITICAL: timestamp + bold_red + loglevel + reset + message
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def _init_logger(level=logging.INFO):
    logger = logging.getLogger()
    logger.setLevel(level)

    formatter = ColorLogFormatter()
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
