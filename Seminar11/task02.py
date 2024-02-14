"""
Создайте класс Архив, который хранит пару свойств. Например, число и строку.
При нового экземпляра класса, старые данные из ранее созданных экземпляров
сохраняются в пару списков-архивов, которые также являются свойствами экземпляра.
"""


class Archive:
    _instance = None

    def __new__(cls, text, name):

        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.all_text = []
            cls._instance.all_name = []
        else:
            cls._instance.all_text.append(cls._instance.text)
            cls._instance.all_name.append(cls._instance.name)
        return cls._instance

    def __init__(self, text: str, name: str):
        self.text = text
        self.name = name


if __name__ == '__main__':
    c = Archive('Hello', 'Jo')
    print(f"{c = }\t{c.all_text = }\t{c.all_name = }\t{type(c)}")
    b = Archive('Good', 'Gregory')
    print(f"{b = }\t{b.all_text = }\t{b.all_name = }\t{type(b)}")
    d = Archive('sdf', 'sdf')
    print(f"{d = }\t{d.all_text = }\t{d.all_name = }\t{type(d)}")
    print(Archive.__dict__)

