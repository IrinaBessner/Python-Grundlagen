# Ein Traceback zeigt, wo ein Fehler aufgetreten ist und welche Funktionsaufrufe zu diesem Fehler geführt haben.

# #Einfach logging.error()
# import logging

# logging.basicConfig(level=logging.DEBUG)
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     logging.error("Division durch Null!")


#logging.exception()
# import logging

# logging.basicConfig(level=logging.DEBUG)
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     logging.exception("Division durch Null!")    



                    #BEISPIEL
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("LoginTest")
def login(username, password):
    logger.info("Login test started")
    try:
        if username == "":
            raise ValueError("Username is empty")
        if password == "":
            raise ValueError("Password is empty")
        logger.info("Login successful")
    except ValueError:
        logger.exception("Login test failed")
login("", "12345")