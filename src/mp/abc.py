class AbstractMethodException(Exception):
    def __init__(self):
        super().__init__('my subclass should have implemented this method')


def abstractmethod(function: callable):
    def objector(*args):
        raise AbstractMethodException()
    return objector


class ABC:
    pass