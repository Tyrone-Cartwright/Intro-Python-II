# Items class


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"{self.name}, {self.description}"


class Treasure(Item):
    def __init__(self, name, description):
        super().__init__(self, name, description)
