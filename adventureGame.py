from typing import List, Dict, Optional


class Player:
    def __init__(self, name: str, health: int, inventory: Optional[List[str]] = None):
        """
        Initialize a Player object.

        Args:
            name (str): The name of the player.
            health (int): The health points of the player.
            inventory (List[str], optional): The initial inventory of the player. Defaults to None.
        """
        self.name = name
        self.health = health
        self.inventory = inventory if inventory is not None else []

    def display_status(self) -> None:
        """Display the player's name, health, and inventory."""
        print(f"Name: {self.name}, Health: {self.health}, Inventory: {self.inventory}")

    def take_damage(self, amount: int) -> None:
        """Reduce the player's health by the specified amount."""
        self.health -= amount

    def heal(self, amount: int) -> None:
        """Increase the player's health by the specified amount."""
        self.health += amount

    def add_to_inventory(self, item: str) -> None:
        """Add an item to the player's inventory."""
        self.inventory.append(item)


class Room:
    def __init__(self, name: str, description: str, items: List[str], exits: Dict[str, str]):
        """
        Initialize a Room object.

        Args:
            name (str): The name of the room.
            description (str): The description of the room.
            items (List[str]): The list of items in the room.
            exits (Dict[str, str]): The dictionary of exit directions mapped to the next room names.
        """
        self.name = name
        self.description = description
        self.items = items
        self.exits = exits

    def display_info(self) -> None:
        """Display information about the room."""
        print(f"Name: {self.name}, Description: {self.description}")
        print(f"Items: {self.items}, Exits: {self.exits}")


class Game:
    def __init__(self, player: Player, start_room: Room):
        """
        Initialize a Game object.

        Args:
            player (Player): The player object.
            start_room (Room): The starting room for the game.
        """
        self.player = player
        self.current_room = start_room

    def move(self, direction: str) -> None:
        """
        Move the player to the next room based on the specified direction.

        Args:
            direction (str): The direction to move ('north', 'south', 'east', 'west').
        """
        if direction in self.current_room.exits:
            next_room_name = self.current_room.exits[direction]
            next_room = predefined_rooms[next_room_name]
            self.current_room = next_room
            print(f"You move {direction} to {next_room_name}.")
        else:
            print("Invalid direction.")

    def take(self, item: str) -> None:
        """
        Allow the player to take an item from the current room.

        Args:
            item (str): The name of the item to take.
        """
        item_lower = item.lower()
        room_items_lower = [i.lower() for i in self.current_room.items]
        if item_lower in room_items_lower:
            actual_item = self.current_room.items[room_items_lower.index(item_lower)]
            self.player.add_to_inventory(actual_item)
            self.current_room.items.remove(actual_item)
            print(f"You take {actual_item}.")
        else:
            print(f"There is no {item} in this room.")

    def use(self, item: str) -> None:
        """
        Allow the player to use an item from their inventory.

        Args:
            item (str): The name of the item to use.
        """
        if item in self.player.inventory:
            if item == "map":
                print("fc-ce-tr\n|\nfe")
            print(f"You use {item}.")
        else:
            print(f"You don't have {item} in your inventory.")

    def display_current_room(self) -> None:
        """Display information about the current room."""
        self.current_room.display_info()


# Define predefined rooms
forest_entrance = Room(
    "Forest Entrance",
    "You find yourself at the entrance of a mysterious forest.",
    items=["map"],
    exits={"north": "Forest Clearing"}
)

forest_clearing = Room(
    "Forest Clearing",
    "A peaceful clearing in the middle of the forest.",
    items=["Sword"],
    exits={"south": "Forest Entrance", "east": "Cave Entrance"}
)

cave_entrance = Room(
    "Cave Entrance",
    "A dark cave entrance with a mysterious aura.",
    items=["Torch"],
    exits={"west": "Forest Clearing", "east": "Treasure Room"}
)

treasure_room = Room(
    "Treasure Room",
    "A room filled with glittering treasures.",
    items=["Treasure"],
    exits={"west": "Cave Entrance"}
)

# Connect the predefined rooms
predefined_rooms = {
    "Forest Entrance": forest_entrance,
    "Forest Clearing": forest_clearing,
    "Cave Entrance": cave_entrance,
    "Treasure Room": treasure_room
}


def main() -> None:
    """Main function to run the text-based adventure game."""
    print("Welcome to the Text-Based Adventure Game!")
    print("You find yourself at the entrance of a mysterious forest.")
    print("Your goal is to explore and collect treasures.")
    print("Commands: move [direction], take [item], use [item], exit\n")

    player = Player("Adventurer", health=100, inventory=[])
    start_room = forest_entrance
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
