from logger import logging
from constants import APP_NAME
from cabs.factories.populate_db import populate_db
from demo import Demo

if __name__ == '__main__':
    logging.info(f"Welcome to {APP_NAME}")
    populate_db()
    Demo.run_demo()
