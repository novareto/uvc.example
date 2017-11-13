import logging
logger = logging.getLogger('uvcsite.uvc.example')

def log(message, summary='', severity=logging.DEBUG):
    logger.log(severity, '%s %s', summary, message)
