import logging
import graypy
import settings


def get_log():
    my_logger = logging.getLogger('test_logger')
    my_logger.setLevel(logging.DEBUG)

    handler = graypy.GELFUDPHandler('localhost', 514, debugging_fields=False)
    my_logger.addHandler(handler)
    
    return my_logger
