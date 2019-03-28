from room import Room
from player import Player
from item import Item

# Declare all the rooms

items = {
    'axe': Item("Axe", "rusty axe with a wooden handle"),
    'sword': Item("Sword", "sword with gold ancient winding grip"),
    'med-kit': Item("Med-kit", "med-kit to heal any wounds"),
    'gun': Item("Gun", ".45 caliber gun full clip"),
    'crowbar': Item("Crowbar", "long crowbar used to open boxes"),
    'key': Item("key", "old dirty key"),
    'brass knuckles': Item("brass knuckles", "brass knuckles"),
    'knife': Item("knife", "a knife"),
    'flashlight': Item("flashlight", "a police flashlight")
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items['axe']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items['gun']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [items['flashlight']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [items['sword']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [items['med-kit']]),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#


# Make a new player object that is currently in the 'outside' room.
name_player = input("Enter player name:")
player = Player(room['outside'], name_player)
print(name_player, 'is in the', room['outside'])


def try_direction(direction, current_room):
    attribute = direction + '_to'

    if hasattr(current_room, attribute):
        return getattr(current_room, attribute)
    else:
        print("You can't move in that direction!")
        return current_room


# Write a loop that:
while True:
    # * Prints the current room name
    print(player.current_room.name)
# * Prints the current description (the textwrap module might be useful here).
    print(player.current_room.description)

# * Waits for user input and decides what to do.
    user_input = input(">").lower().split()
    print(user_input)

    if user_input == "q":
        break

    elif len(user_input) == 1:
        user_input = user_input[0][0]
        player.current_room = try_direction(user_input, player.current_room)

    elif len(user_input) == 2:
        action = user_input[0]
        item = user_input[1]

        if action == "take":
            if item in player.current_room.items:
                player.current_room.items.remove(item)
                player.inventory.append(item)
                print(f"{item.name} was added to your inventory")

            elif action == "drop":
                if item in player.inventory:
                    player.inventory.remove(item)
                    player.current_room.items.append(item)
                    print(f"{item.name} was dropped from your inventory")

    else:
        print("I didn't quite get that")
