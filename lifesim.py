#Life Simulator Verson 0.1.0

import random

player_name = input("Enter character name: ")
age = 18
health = random.randint(50, 100)
wealth = random.randint(1000, 5000)
happiness = random.randint(50, 100)
intelligence = random.randint(50, 100)
playergender = input("Enter your Gender: ")
print(f"Welcome {player_name}! Your life begins now...")
print(f"Your Stats - Age: {age}, Health: {health}, Wealth: ${wealth}, Happiness: {happiness}, Intelligence: {intelligence}, Gender: {playergender}")
joborcollege = "Do you want to go to college or start working? (college/work): "
if input(joborcollege).lower() == "college":
        print("You chose college. You spend 4 years studying and graduate with a degree.")
        age += 4
        wealth -= 20000
        if wealth < 0:
            wealth = 0
        intelligence += 20
        if intelligence > 100:
            intelligence = 100
else:
        print("You chose to work. You gain experience but miss out on college life.")
while True:
    print(f"Your Stats - Age: {age}, Health: {health}, Wealth: ${wealth}, Happiness: {happiness}, Intelligence: {intelligence}")
    print("What do you want to do?")
    print("1. Work")
    print("2. Rest")
    print("3. Age up")
    print("4. Quit")

    choice = input("> ")

    if choice == "1":
        wealth += random.randint(10, 100)
        health -= random.randint(5, 15)
        if health < 0:
            health = 0
        print("You worked hard and earned some money.")

    elif choice == "2":
        health += random.randint(10, 30)
        if health > 100:
            health = 100
        print("You rested and regained health.")

    elif choice == "3":
        age += 1
        print("You got older...")

    elif choice == "4":
        print("Thanks for playing!")
        break

    else:
        print("Invalid choice.")