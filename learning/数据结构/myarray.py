class Myarray:
    """
    a simple wrapper around list
    you cannot have -1 in the array
    """

    def __init__(self, capacity: int):
        self._data = []
        self._capacity = capacity

    def __getitem__(self, position: int) -> object:
        return self._data[position]

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self):
        for item in self._data:
            yield item

    def find(self, index: int) -> object:
        try:
            return self._data[index]
        except IndexError:
            return None

    def delete(self, index: int) -> bool:
        try:
            self._data.pop(index)
            return True
        except IndexError:
            return False

    def insert(self, index: int, value: int) -> bool:
        if len(self) >= self._capacity:
            return False
        else:
            return self._data.insert(index, value)

    def print_all(self):
        for x in self._data:
            print(x)


if __name__ == '__main__':
    arr = Myarray(5)
    arr.insert(0, 1)
    arr.insert(4, 4)
    arr.insert(0, 3)
    arr.insert(0, 2)
    arr.insert(8, 8)

    arr.print_all()
    assert arr.insert(8, 8) is False
    assert arr.delete(4) is True
    arr.delete(0)
    arr.print_all()


