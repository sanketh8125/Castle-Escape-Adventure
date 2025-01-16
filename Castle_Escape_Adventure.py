import random

def character_creation():
    """
    Allows the player to create their character by entering a name and selecting a role.
    Default role is 'warrior' if an invalid role is chosen.
    
    Returns:
        tuple: A tuple containing the character's name and role.
    """
    print("Before we begin, let's create your character.")
    name = input("Enter your character's name: ").strip()
    role = input("Choose your role (warrior/mage/rogue): ").strip().lower()
    if role not in ["warrior", "mage", "rogue"]:
        print("Invalid role. Defaulting to 'warrior'.")
        role = "warrior"
    print(f"\nWelcome, {name} the {role}! Your adventure begins now...")
    return name, role

def intro():
    """
    Displays the introduction to the game, setting the scene and explaining the objective.
    """
    print("Welcome to the Castle Escape Adventure!")
    print("You wake up in a mysterious castle with no memory of how you got there.")
    print("Your goal is to find your way out of the castle by solving puzzles and making choices.")
    input("Press Enter to begin your adventure...\n")

def room_one():
    """
    Represents the first room in the game: a hallway with three doors.
    The player selects one of the shuffled doors to proceed.

    Returns:
        function/bool: Calls the next room function or ends the game if a losing door is chosen.
    """
    print("\nRoom 1: The Hallway")
    print("You find yourself in a dimly lit hallway. There are three doors: one to your left, one to your right, and one straight ahead.")
    doors = ["left", "right", "middle"]
    random.shuffle(doors)
    print(f"The doors are labeled: {', '.join(doors)}")
    choice = input("Do you choose the left door, the right door, or the middle door? (left/right/middle): ").strip().lower()
    if choice == doors[0]:
        print("You enter a room filled with strange symbols on the walls.")
        return room_two()
    elif choice == doors[1]:
        print("You step into a dark room and the door locks behind you. Game over.")
        return False
    elif choice == doors[2]:
        print("You find yourself in a cozy library with a glowing book on a pedestal.")
        return library_room()
    else:
        print("Invalid choice. Try again.")
        return room_one()

def room_two():
    """
    Represents the second room: a puzzle room.
    The player solves a math puzzle to unlock a box and proceed.

    Returns:
        function/bool: Calls the next room function if the puzzle is solved or ends the game if the answer is incorrect.
    """
    print("\nRoom 2: The Puzzle Room")
    print("In the center of the room, there's a pedestal with a locked box. The box has a keypad.")
    print("A math puzzle is written on the wall: 'I am a three-digit number. My tens digit is five more than my ones digit, and my hundreds digit is eight less than my tens digit. What am I?'")
    answer = input("Enter your answer: ").strip()
    if answer == "194":
        print("The box unlocks, revealing a golden key.")
        return room_three_with_twist()
    else:
        print("The box remains locked. You cannot proceed. Game over.")
        return False

def library_room():
    """
    Represents the second room: a library.
    The player solves a math puzzle written in a glowing book to proceed.

    Returns:
        function/bool: Calls the next room function if the puzzle is solved or ends the game if the answer is incorrect.
    """
    print("\nRoom 2: The Library")
    print("The glowing book on the pedestal has an inscription: 'Solve this to proceed: I am a number. Multiply me by 4, then subtract 6, and you get 42. What am I?'")
    answer = input("Enter your answer: ").strip()
    if answer == "12":
        print("The book flips open, revealing a silver key hidden inside.")
        return room_three_with_twist()
    else:
        print("The book remains shut, and the room darkens. Game over.")
        return False

def room_three_with_twist():
    """
    Represents the final room: a large door with a keyhole and a riddle.
    The player solves the riddle to unlock the door and win the game.

    Returns:
        bool: True if the player wins, False if the answer is incorrect.
    """
    print("\nRoom 3: The Final Door")
    print("You arrive at a large door with a keyhole. This must be the way out.")
    print("But there is a riddle on the door: 'Divide 100 by half and add 30. What is the answer?'")
    answer = input("Enter your answer: ").strip()
    if answer == "230":
        print("The door creaks open, revealing the sunlight outside. You have escaped the castle. Congratulations, you win!")
        return True
    else:
        print("The door remains locked. You cannot proceed. Game over.")
        return False

def main():
    """
    Main function to run the game.
    Handles character creation, introduction, and room transitions.
    Displays appropriate end messages based on the player's success or failure.
    """
    name, role = character_creation()
    intro()
    if room_one():
        print(f"\nThank you for playing Castle Escape Adventure, {name} the {role}!")
    else:
        print(f"\nBetter luck next time, {name} the {role}!")

if __name__ == "__main__":
    main()
