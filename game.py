class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def add_paths(self, paths):
        self.paths.update(paths)


def start():
    rooms = {
        'start': Room("Start", "You find yourself in a dark room."),
        'hallway': Room("Hallway", "You are in a long hallway."),
        'treasure': Room("Treasure Room", "You've found the treasure room!")
    }

    rooms['start'].add_paths({'east': rooms['hallway']})
    rooms['hallway'].add_paths({'west': rooms['start'], 'north': rooms['treasure']})

    current_room = rooms['start']

    while True:
        print("\n" + current_room.name)
        print(current_room.description)
        command = input("What do you do? (Enter a direction or 'quit'): ")

        if command == 'quit':
            break
        elif command in current_room.paths:
            current_room = current_room.paths[command]
        else:
            print("Invalid direction. Try again.")

if __name__ == "__main__":
    start()

