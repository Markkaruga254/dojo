"""Lab 02: retry decorator."""
from __future__ import annotations

import time


def retry(times: int = 3, base_delay: float = 0.1, exceptions: tuple = (Exception,),
          sleep=time.sleep):
    """Decorator factory.

    Call the function up to `times` attempts in total. After a failed attempt k (1-based) that is
    not the last, call sleep(base_delay * 2 ** (k - 1)). Only retry exceptions in `exceptions`;
    anything else propagates immediately. After the final failed attempt re-raise the last
    exception. Preserve __name__ and __doc__ (functools.wraps). Return the function's value on success.
    """
    raise NotImplementedError
