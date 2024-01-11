#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Player:
    def __init__(self, name: str, health: int, inventory: list = None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory
        self.name = name
        self.health = health

    def display_status(self):
        print("Name:", self.name, "Health:", self.health, end=" ")
        print("Inventory:", self.inventory)

    def take_damage(self, amount: int):
        self.health -= amount

    def heal(self, amount: int):
        self.health += amount

    def add_to_inventory(self, item):
        self.inventory.append(item)


class Room:
    def __init__(self, name: str, description: str, items: list, exits: dict):
        self.name = name
        self.description = description
        self.items = items
        self.exits = exits

    def display_info(self):
        print("Name:", self.name, "Description:", self.description,
              "Items:", self.items, "Exits:", self.exits)


class Game:
    def __init__(self, player: Player, start_room: Room):
        self.player = player
        self.current_room = start_room

    def move(self, direction):
        if direction in self.current_room.exits:
            next_room_name = self.current_room.exits[direction]
            # Assume all rooms are predefined
            next_room = predefined_rooms[next_room_name]
            self.current_room = next_room
            print(f"You move {direction} to {next_room_name}.")
        else:
            print("Invalid direction.")

    def take(self, item):
        item_lower = item.lower()  # Convert input to lowercase
        room_items_lower = [i.lower() for i in
                            self.current_room.items]  # Convert room items to lowercase for comparison

        if item_lower in room_items_lower:
            # Find the actual item name in the original case
            actual_item = self.current_room.items[room_items_lower.index(item_lower)]
            self.player.add_to_inventory(actual_item)
            self.current_room.items.remove(actual_item)
            print(f"You take {actual_item}.")
        else:
            print(f"There is no {item} in this room.")

    def use(self, item):
        if item in self.player.inventory:
            print(f"You use {item}.")
            # Implement logic for using items if needed
        else:
            print(f"You don't have {item} in your inventory.")

    def display_current_room(self):
        self.current_room.display_info()


# Define predefined rooms
forest_clearing = Room("Forest Clearing", "A peaceful clearing in the middle of the forest.",
                       items=["Sword"], exits={"south": "Forest Entrance"})
cave_entrance = Room("Cave Entrance", "A dark cave entrance with a mysterious aura.",
                     items=["Torch"], exits={"north": "Forest Entrance", "east": "Treasure Room"})
treasure_room = Room("Treasure Room", "A room filled with glittering treasures.",
                     items=["Treasure"], exits={"west": "Cave Entrance"})

# Connect the predefined rooms
predefined_rooms = {
    "Forest Entrance": forest_clearing,
    "Forest Clearing": cave_entrance,
    "Cave Entrance": cave_entrance,
    "Treasure Room": treasure_room
}



def main():
    print("Welcome to the Text-Based Adventure Game!")
    print("You find yourself at the entrance of a mysterious forest.")
    print("Your goal is to explore and collect treasures.")
    print("Commands: move [direction], take [item], use [item], exit\n")

    player = Player("Adventurer", health=100, inventory=[])
    start_room = Room("Forest Entrance", "You find yourself at the entrance of a mysterious forest.",
                      items=["map"], exits={"north": "Forest Clearing"})
    game = Game(player, start_room)

    # Play the game
    while True:
        game.display_current_room()
        game.player.display_status()
        action = input("Enter your action: ").lower().split()

        if not action:
            print("Invalid input. Try again.")
            continue

        verb = action[0]

        if verb == "exit":
            print("Exiting the game. Goodbye!")
            break
        elif verb == "move":
            if len(action) == 2:
                direction = action[1]
                game.move(direction)
            else:
                print("Invalid input. Try again.")
        elif verb == "take":
            if len(action) == 2:
                item = action[1]
                game.take(item)
            else:
                print("Invalid input. Try again.")
        elif verb == "use":
            if len(action) == 2:
                item = action[1]
                game.use(item)
            else:
                print("Invalid input. Try again.")
        else:
            print("Invalid action. Try again.")


if __name__ == "__main__":
    main()
