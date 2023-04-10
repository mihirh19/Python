"""In Python, getters and setters are special methods that allow us to control access to the attributes of an object.
They provide an additional layer of abstraction by allowing us to define custom behavior for getting and setting the
values of object attributes. Getters are used to retrieve the value of an attribute, while setters are used to modify
the value of an attribute."""


class Demo:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"value is {self._value}")

    @property
    def privateer(self):
        return self._value

    @privateer.setter
    def privateer(self, value):
        self._value = value


if __name__ == '__main__':
    c = Demo(32)

    print(c.privateer)
    c.privateer = 100
    print(c.privateer)
