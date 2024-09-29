from difflib import get_close_matches
from predefined_animals import get_predefined_animals
from data_driven import get_animals_data
from utils import print_verse

# Predefined lists for validation and suggestions
VALID_ANIMALS = [
    "cow", "dog", "cat", "pig", "duck", "sheep", "horse", "goat", "chicken", "turkey",
    "rabbit", "frog", "lion", "elephant", "bear"
]
VALID_SOUNDS = [
    "moo", "bark", "meow", "oink", "quack", "baa", "neigh", "bleat", "cluck", "gobble",
    "hop", "ribbit", "roar", "trumpet", "growl"
]

def get_user_animals():
    """Allow user to add custom animals and their sounds."""
    animals_data = {}

    while True:
        try:
            num_of_animals = int(input("How many animals would you like to add? "))
            if num_of_animals <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    for _ in range(num_of_animals):
        # Validate animal name input
        while True:
            animal_name = input("Enter the name of an animal: ").strip().lower()
            if animal_name.isalpha() and animal_name in VALID_ANIMALS:
                break
            else:
                # Suggest close matches
                suggestions = get_close_matches(animal_name, VALID_ANIMALS)
                if suggestions:
                    print(f"Invalid input! Did you mean: {', '.join(suggestions)}?")
                else:
                    print("Invalid input! Please enter a valid animal name (letters only).")

        # Validate sound input
        while True:
            sound = input(f"Enter the sound that a {animal_name} makes: ").strip().lower()
            if sound.isalpha() and sound in VALID_SOUNDS:
                break
            else:
                # Suggest close matches
                suggestions = get_close_matches(sound, VALID_SOUNDS)
                if suggestions:
                    print(f"Invalid input! Did you mean: {', '.join(suggestions)}?")
                else:
                    print("Invalid input! Please enter a valid sound (letters only).")

        animals_data[animal_name] = sound

    return animals_data

def main():
    print("Choose an approach:")
    print("1. Use predefined animals (polymorphism-based solution).")
    print("   This will use a set list of animals with their sounds defined in classes.")
    print("2. Use a data-driven approach.")
    print("   This will use a dictionary to define animals and their sounds.")
    print("3. Enter your own animals.")
    print("   This allows you to provide custom animals and their sounds.")

    choice = input("Enter 1, 2 or 3: ").strip()

    if choice == '1':
        # Polymorphism-based solution
        animals = get_predefined_animals()
        for animal in animals:
            print_verse(animal.name, animal.make_sound())

    elif choice == '2':
        # Data-driven solution
        animals_data = get_animals_data()
        for animal, sound in animals_data.items():
            print_verse(animal, sound)

    elif choice == '3':
        # User input for custom animals and sounds
        animals_data = get_user_animals()
        for animal, sound in animals_data.items():
            print_verse(animal, sound)

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
