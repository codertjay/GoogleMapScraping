import signal
import time

timeout_duration = 8


class TimeoutException(Exception):
    """Exception class for a timeout"""
    pass


def timeout_handler(signum, frame):
    """Handler function to be called when alarm signal is received"""
    raise TimeoutException()


def test():
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(5)
    time.sleep(6)
    signal.alarm(0)
    return


test()
