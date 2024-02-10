class DataPerson:

    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.__age = age

    def birthday(self):
        self.__age += 1

    def __str__(self):
        return f"{self.name} {self.surname} {self.__age}"


if __name__ == '__main__':
    human_1 = DataPerson('Petr', 'Petrov', 27)
    human_2 = DataPerson('Sergey', 'Serov', 30)
    print(human_1)
    print(human_2)
