# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, area, description, items):
        self.area = area
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items_in_room = items

    def hasItem(self, item):
        for i in self.items_in_room:
            if i.name.lower() == item.lower():
                return True
        return False

    def getItems(self):
        if len(self.items_in_room) == 0:
            return "nothing"
        output = "a "
        if len(self.items_in_room) == 1:
            output += self.items_in_room[0].name
            return output
        else: 
            for i in self.items_in_room:
                if i == self.items_in_room[-1]:
                    output += "and a " + i.name
                    if len(self.items_in_room) == 2:
                        output = output.replace(",","")
                    return output
                output += i.name + ", "
                
            

