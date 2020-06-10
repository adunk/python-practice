import logging

ext_data = {
    'user': 'Andrew Dunkle'
}


def anotherFunction():
    logging.debug('This is a debug-level message.', extra=ext_data)


def main():
    # %(asctime)s - Human readable date format when the log record was created
    # %(filename)s - Filename where the log message originated
    # %(funcName)s - Function name where the log message originated
    # %(levelname)s - String representation of the message level
    # %(levelno)s - Numeric representation of the message level
    # %(lineno)s - Source line number where the logging call was used
    # %(message)s - The logged message string itself
    # %(module)s - Module name portion of the filename where the message was logged
    fmtstr = 'User:%(user)s %(asctime)s: %(levelname)s: %(funcName)s Line:%(levelno)s %(message)s'
    datestr = '%m/%d/%Y %I:%M:%S %p'
    logging.basicConfig(level=logging.DEBUG, filename='output.log', filemode='w', format=fmtstr, datefmt=datestr)

    # Diagnostic information useful for debugging
    logging.debug('This is a debug message', extra=ext_data)
    # General information about program execution
    logging.info('This is an info message', extra=ext_data)
    # Something unexpected, or approaching a problem
    logging.warning('This is a warning message', extra=ext_data)
    # Unable to perform a specific operation due to problem
    logging.error('This is an error message', extra=ext_data)
    # Program may not be able to continue, serious error
    logging.critical('This is a critical message', extra=ext_data)

    anotherFunction()


if __name__ == '__main__':
    main()
