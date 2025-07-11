import logging

#for writing the log messages to the text file
logging.basicConfig(filename='my_program_log.txt', level=logging.DEBUG, format=' %(asctime)s - %(message)s')
"""
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

"""
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(' + str(n) + ')')
    total = 1
    # Change the 'for i in range(n + 1):' line to 'for i in range(1, n + 1):' for correction
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(' + str(n) + ')')
    return total

print(factorial(5))
logging.debug('End of program')