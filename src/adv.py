from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("Holy Locket", "A healing charm"), Item("Tribal Drum", "A tribal drum"), Item("Helm of the Dominator", "A powerful helmet that gives the ability to control minds")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
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

player = Player("Nereid", room["outside"])
move = ""
while move != "q":
    
    print(f"You are in the {player.current_room.area}")
    print(f"You see {player.current_room.getItems()} laying around")
    print(f"{player.current_room.description}")

    move = input("~~> ")

    if len(move.split()) > 1:
        print (move.split())
        if move.split()[0] == "take" or move.split()[0] == "get":
            player.take(" ".join(move.split()[1:]))
    elif move =="n":
        if player.current_room.n_to is not None:
            player.current_room = player.current_room.n_to
        else:
            print ("There is nothing in that direction.")
    elif move == "s":
        if player.current_room.s_to is not None:
            player.current_room = player.current_room.s_to
        else:
            print ("There is nothing in that direction.")
    elif move == "e":
        if player.current_room.e_to is not None:
            player.current_room = player.current_room.e_to
        else:
            print ("There is nothing in that direction.")
    elif move == "w":
        if player.current_room.w_to is not None:
            player.current_room = player.current_room.w_to
        else:
            print ("There is nothing in that direction.")
    elif move == "q":
        print("gg wp")
        exit()
    else:
        print("Valid moves are n,s,e, or w")