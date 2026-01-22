#Life Simulator Verson 0.1.1

import random

player_name = input("Enter character name: ").strip().title()
playergender = input("Enter your Gender: ").strip().title()
age = 18
health = random.randint(50, 100)
wealth = random.randint(1000, 5000)
happiness = random.randint(50, 100)
intelligence = random.randint(50, 100)
life_end = random.randint(90, 110)

def print_stats():
    print(f"Your Stats - Age: {age}, Health: {health}, Wealth: ${wealth}, Happiness: {happiness}, Intelligence: {intelligence}, Gender: {playergender}")

def cap_stats():
    global health, intelligence, happiness, wealth
    health = min(max(health, 0), 100)
    intelligence = min(max(intelligence, 0), 100)
    happiness = min(max(happiness, 0), 100)
    wealth = max(wealth, 0)

def work_stats():
    global wealth, health, happiness, intelligence
    wealth += random.randint(10, 100)
    health -= random.randint(5, 15)
    happiness -= random.randint(1, 5)
    intelligence += random.randint(0,2)
    cap_stats()
    print("You worked hard and earned some money.")

def rest_stats():
    global health, happiness
    health += random.randint(10, 30)
    happiness += random.randint(1, 5)  
    cap_stats()
    print("You took a day for yourself! You feel much better.")

def go_to_dr():
    global health, wealth
    health += random.randint(50, 80)
    wealth -= 500
    cap_stats()
    print("You went to the Doctor. Your health has improved, but it cost you $500.")

def study():
    global intelligence, happiness
    intelligence += random.randint(25, 40)
    happiness += random.randint(5, 15)
    cap_stats()
    print("You studied and increased your intelligence. You now feel better about yourself!")

def age_stats():
    global health, age, happiness
    age += 1
    health_loss = random.randint(0, 2)
    health -= health_loss
    
    if age >= 50:
        health -= 10
        happiness -= random.randint(0, 10)

        print("Ouch... I'm old.")

    cap_stats()
    print("You got older! Happy Birthday!")

def you_died():
    if health <= 0:
        print("You died. Game over :(")
        return True
    if happiness <= 0:
        print("You are too sad to live. You died :(")
        return True
    return False

def game_win():
    if age >= life_end and health > 0:
         print(f"Rest in peace, {player_name}. You have lived a good life and passed away from old age.")
         return True
    return False

def check_game_over():
    if you_died() or game_win():
        return True
    return False

def warnings():
    if health <= 20:
        print("You are getting very sick. Please take a break or go to the doctor.")
    if happiness <= 20:
        print("You are feeling sad. Please take a break for yourself before it gets too bad.")
    if wealth <= 1000:
        print(f"You have ${wealth}. Consider working harder or managing your expenses.")
    if intelligence <= 30:
        print("Your intelligence is low. Please consider studying.")

def critical_warnings():
    global choice
    if health <= 10:
        print("WARNING!! You are CRITICALLY ill. Visit the doctor IMMEDIATELY!!")
        critical = input("Would you like to go to the Doctor? (Yes/No): ").strip().lower()
        if critical == "yes":
            go_to_dr()
            return True
    
    if happiness <= 10:
        print("DANGER. You are EXTREMELY unhappy!! Please take a mental health day immediately.")
        critical = input("Would you like to rest today? (Yes/No): ").strip().lower()
        if critical == "yes":
            rest_stats()
            return True

    if wealth <= 100:
        print(f"You have ${wealth}. You are going to go bankrupt, {player_name}.")
        critical = input("Would you like to go to work? (Yes/No): ").strip().lower()
        if critical == "yes":
            work_stats()
            return True

    if intelligence <= 10:
        print("Your intelligence is dangerously low. Please, pick up a book or something?")
        critical = input("Would you like to study? (Yes/No): ")
        if critical == "yes":
            study()
            return True

    return False
         

    
print(f"Welcome {player_name}! Your life begins now...")
print_stats()

while True:
    joborcollege = input("Do you want to go to college or start working? (college/work): ").strip().lower()
    if joborcollege in ["college", "work"]:
        break
    print("Invalid option. Please type either 'college' or 'work'.")

if joborcollege == "college":
    print("You chose college. You spend 4 years studying and graduate with a degree!")
    age += 4
    wealth -= 20000
    intelligence += 20
    happiness += 10
    health -= 15
    cap_stats()
else:
    print("You chose to work. You gain experience but miss out on college life.")
    wealth += 5000
    happiness -= 5
    cap_stats()

while True:
    if critical_warnings():
        continue
    warnings()
    print_stats()
    print("1. Work")
    print("2. Rest")
    print("3. Age up")
    print("4. Go to the Doctor")
    print("5. Study")
    print("6. Quit")

    choice = input("> ")

    if choice == "1":
        work_stats()

    elif choice == "2":
        rest_stats()

    elif choice == "3":
        age_stats()

    elif choice == "4":
        go_to_dr()

    elif choice == "5":
        study()

    elif choice == "6":
        print("Thanks for playing!")
        break

    else:
        print("Invalid Choice.")

    if check_game_over():
        break
