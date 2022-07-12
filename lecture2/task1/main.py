class CyclicIterator:

    def __init__(self, iter_object):
        self.input_data = [value for value in iter_object]
        self.iter_value = iter(self.input_data)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            value = next(self.iter_value)
        except StopIteration:
            self.iter_value = iter(self.input_data)
            value = next(self.iter_value)
            return value
        else:
            return value


if __name__ == '__main__':
    cyclic_iterator = CyclicIterator(range(3))
    for i in cyclic_iterator:
        print(i)
