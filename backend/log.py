import logging
import sys
import time


def config_logger():
    """Init the configuration of root logger.

    """

    # Get root logger.
    logger = logging.getLogger()
    handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(handler)

    # Set formatter
    # Example: 2019-03-14 08:25:45 CET 366 INFO [__main__]: Bala bala.    (xxx.py:1796)
    formatter = logging.Formatter(
        fmt='%(asctime)s {timezone} %(levelname)s [%(name)s]: %(message)s    (%(filename)s:'
            '%(lineno)d)'.format(timezone=time.strftime('%Z', time.localtime(time.time()))))
    handler.setFormatter(formatter)

    # Set init level as INFO.
    logger.setLevel(logging.INFO)