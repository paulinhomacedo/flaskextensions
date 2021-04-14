import time

import schedule
from dynaconf import settings

from fexservice.consumer import fetch_github
from fexservice.logger import logger

logger.info(
    f"The DELAY was set to {settings.DELAY} seconds"
    + f"and PRIORITY to {settings.PRIORITY}"
)


def job():
    fetch_github()

schedule.every(settings.DELAY).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
