# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, current_room, name):
        self.name = name
        self.inventory = []
        self.current_room = current_room

    def move(self, current_room):
        self.current_room = self.current_room.new_room(room)
