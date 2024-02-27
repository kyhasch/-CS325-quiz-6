from abc import ABC, abstractmethod

# Abstract logging interface
class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

# Implementation of Logger using the logging library
class LoggingLogger(Logger):
    def log(self, message):
        print("Logging: ", message)
        # You would integrate your actual logging library here
        # Example: logging.info(message)

# Implementation of Logger using the loguru library
class LoguruLogger(Logger):
    def log(self, message):
        print("Loguru: ", message)
        # Example: logger.info(message)

# Application logic
class SomeClass:
    def __init__(self, logger):
        self.logger = logger

    def do_something(self):
        self.logger.log("Doing something...")

def main():
    # Instantiate the logger implementation based on configuration or preferences
    logger = LoggingLogger()  # Or LoguruLogger()

    # Pass the logger implementation to the application logic
    obj = SomeClass(logger)
    obj.do_something()

if __name__ == "__main__":
    main()
