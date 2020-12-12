import asyncio
import logging
# missing the following import statements
import os
import datetime

logger = logging.getLogger(__name__)
SLEEP_DURATION = os.getenv("SLEEP_DURATION")

class Pipeline:
    # missing self as first argument in __init__ and sleep_for
    # __init__ must be synchronous
    def __init__(self, *args, **kwargs):
        default_sleep_duration = kwargs["default_sleep_duration"]

    async def sleep_for(self, coro, sleep_duration, *args, **kwargs):
        # missing await before asyncio.sleep() function call
        await asyncio.sleep(sleep_duration)
        logger.info(f"Slept for {sleep_duration} seconds")
        start = datetime.now()
        # missing 's' in **kwargs
        await coro(*args, **kwargs)
        end = datetime.now()
        time_elapsed = (start - end).total_seconds()
        logger.info(f"Executed the coroutine for {time_elapsed} seconds")