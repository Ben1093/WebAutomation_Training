# 1. Virtual Env.
#  which helps us to isolate Environment
#  Virtualenv can active and deactive using command

# Logging means - you can add logs to the failure, information, erro, Warning to the users

import logging

def test_print_logs():
    LOGGER = logging.getLogger(__name__)
    LOGGER.info("This is a information logs")
    LOGGER.error("This is error logs")
    LOGGER.warning("This is a Warning logs")
    LOGGER.critical("This is critical logs")



