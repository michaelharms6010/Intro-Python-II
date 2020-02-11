# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.inventory = []
    def take(self, item):
        print(item)
        for i in self.current_room.items_in_room:
            print(i.name)
            print(item)
            if item == i.name:
                self.inventory.append(i)
                self.current_room.items_in_room.remove(i)
                i.on_take()
        print(f"You don't see {item} here.")