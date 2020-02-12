from room import Room
from player import Player
from item import Item
import random
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("butterfly", "A friendly companion"), Item("tribal drum", "covered in etchings and inscriptions in an unknown language"), Item("Helm of the Dominator", "A powerful helmet that gives the ability to control minds")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Holy Locket", "A healing charm")]),
    'mirrors':    Room("Hall of Mirrors", """Thousands of mirrors surround you. You instantly lose your bearings. You do not remember from which way you entered.""", []),
}


# Link rooms together

mirror_exits = ["foyer", "outside", "treasure"]

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['mirrors']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['mirrors']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room["mirrors"].s_to= room[random.choice(mirror_exits)]
room["mirrors"].n_to= room[random.choice(mirror_exits)]
room["mirrors"].e_to= room[random.choice(mirror_exits)]
room["mirrors"].w_to= room[random.choice(mirror_exits)]


player = Player("Nereid", room["outside"])
move = ""
while move != "q":

    if room["overlook"].hasItem("Butterfly"):
        print("""You free the butterfly on the other side of the foul castle. 
As you watch it flit and flutter into the distance, you realize that life is too beautiful to spend it crawling in dungeons. 
By your great wisdom, you have won the game.""")
        exit()
    
    if player.current_room.area == "Grand Overlook" and player.hasItem("Butterfly"):
            print("You hear a tiny voice within your pocket say 'This is my home! Free me!'")

    if player.current_room == room["mirrors"]:
        if player.hasItem("Holy Locket"):
            player.current_room.description = "Thousands of mirrors surround you. You can easily see where they begin and end."
            print("The Holy Locket has blessed you with acute sight! The illusions of the mirrors have no effect on you.")
            room["mirrors"].s_to= room["foyer"]
            room["mirrors"].n_to= room["overlook"]
            room["mirrors"].e_to= room["treasure"]
            room["mirrors"].w_to= None
        else:
            player.current_room.description = """Thousands of mirrors surround you. You instantly lose your bearings. You do not remember from which way you entered."""
            room["mirrors"].s_to= room[random.choice(mirror_exits)]
            room["mirrors"].n_to= room[random.choice(mirror_exits)]
            room["mirrors"].e_to= room[random.choice(mirror_exits)]
            room["mirrors"].w_to= room[random.choice(mirror_exits)]
    
    print(f"You are in the {player.current_room.area}")
    print(f"You see {player.current_room.getItems()} laying around")
    print(f"{player.current_room.description}")

    move = input("~~> ")

    if len(move.split()) > 1:
        if move.split()[0] == "take" or move.split()[0] == "get":
            player.take(" ".join(move.split()[1:]))
        if move.split()[0] == "drop":
            player.drop(" ".join(move.split()[1:]))
    elif move =="i":
        print(player.getInventory())

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