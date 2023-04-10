class Person:
    name = "Mihir"
    occupation = "developer"
    networth = 1000000

    def info(self):
        print(f"{self.name} is {self.occupation} and {self.networth}")


if __name__ == '__main__':
    a = Person()
    a.name = "Mihir"

    print(a.occupation)
    a.info()
