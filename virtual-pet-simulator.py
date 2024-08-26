# Virtual Pet Simulator

class Pet:
    def __init__(self, name, pet_type):
        self.name = name
        self.pet_type = pet_type
        self.hunger = 50
        self.happiness = 50
        self.health = 50

    def feed(self):
        print(f"\nYou feed {self.name}.")
        self.hunger = min(self.hunger + 10, 100)
        self.happiness = min(self.happiness + 5, 100)

    def play(self):
        print(f"\nYou play with {self.name}.")
        self.happiness = min(self.happiness + 10, 100)
        self.hunger = max(self.hunger - 5, 0)

    def give_medicine(self):
        print(f"\nYou give medicine to {self.name}.")
        self.health = min(self.health + 10, 100)
        self.happiness = max(self.happiness - 5, 0)

    def status(self):
        print(f"\nPet Name: {self.name} | Type: {self.pet_type}")
        print(f"Hunger: {self.hunger} | Happiness: {self.happiness} | Health: {self.health}")

def start_game():
    print("Welcome to the Virtual Pet Simulator!")
    name = input("What would you like to name your pet? ")
    pet_type = input("What type of pet is it? (e.g., cat, dog, dragon) ")

    pet = Pet(name, pet_type)

    while True:
        pet.status()
        print("\nWhat would you like to do?")
        print("1. Feed your pet")
        print("2. Play with your pet")
        print("3. Give your pet medicine")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.give_medicine()
        elif choice == "4":
            print("Goodbye! Thanks for playing the Virtual Pet Simulator.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Start the game
start_game()
