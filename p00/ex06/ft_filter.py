class Ft_Filter:
    def __init__(self, func, iterable):
        self.func = func
        self.iterable = iterable
        self._iterator = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            item = next(self._iterator)
            if self.func is None or self.func(item):
                return item

    def __repr__(self):
        return f'<ft_filter object at {hex(id(self))}>'


def ft_filter(func, iterable):
    """Construct an iterator from those elements of
    iterable for which func returns true."""
    return Ft_Filter(func, iterable)
