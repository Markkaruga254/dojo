# Lab 02: Retry decorator
Implement `retry` in `retry.py`: exponential backoff, selective exceptions, injectable `sleep` for tests, `functools.wraps`.
Think: why is `sleep` a parameter? What changes if you add jitter? (Add it as a stretch, with a seedable RNG.)
