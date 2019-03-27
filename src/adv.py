from room import Room
from player import Player
from item import Item

# Declare all the rooms

# items = {
#     'axe': Item("Axe", "rusty axe with a wooden handle"),
#     'sword': Item("Sword", "sword with gold ancient winding grip"),
#     'med-kit': Item("Med-kit", "med-kit to heal any wounds"),
#     'gun': Item("Gun", ".45 caliber gun full clip"),
#     'crowbar': Item("Crowbar", "long crowbar used to open boxes")
# }

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

# hasattr

# getattr

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'], 'Tyrone')
print(player.name, 'is in the', player.room)

# Write a loop that:
while True:
    #
    # * Prints the current room name
    print(f'Location: {player.room.name[0]}')
# * Prints the current description (the textwrap module might be useful here).
    print(f'Description: {player.room.description}')

# Direction
 print(
        '''Please select whether you want to move "n" for  North, "s" for South, "e" for East, "w" for West''')
# * Waits for user input and decides what to do.
   
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
print('Enter "q" to quit the game.')
