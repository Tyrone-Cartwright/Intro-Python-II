# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, current_room, name, inventory=[]):
        self.name = name
        self.inventory = inventory
        self.current_room = current_room

    # def travel(self, direction):
    #     '''
    #     Moves the player in specified direction
    #     '''
    #     if direction in ["n", "s", "e", "w"]:
    #         next_room = self.current_room.get_room_in_direction(direction)
    #         if next_room is not None:
    #             self.current_room = next_room
    #         else:
    #             print("You cannot move in that direction")
