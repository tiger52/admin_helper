import logging

#logging.basicConfig(format = '%(asctime)s %(levelname)-8s %(message)s', level = logging.INFO, filename = 'Blackout.log')\

blackoutlog = logging.getLogger('blackout')

# file handler
fh = logging.FileHandler('Blackout.log')
frmt = logging.Formatter('%(asctime)s - %(levelname)-8s - %(message)s')
fh.setFormatter(frmt)
# Add this handler to the logger
blackoutlog.addHandler(fh)
blackoutlog.setLevel(logging.INFO)

blackoutlog.debug('test debug level')
#blackoutlogger.info('test blackout log info level')

