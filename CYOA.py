import random
import time
import os
import Slot_Machine_CYOA as slots

# Other entities
begger = {
    "name": "begger",
    "health": 5,
    "strength": 3,
    "speed": 3,
}

# Enemies
lion_lvl1 = {
        "name": "lion",
        "health": 10,
        "strength": 8,
        "speed": 8,
        "drops": "raw meat"
    }
tiger_lvl1 = {
        "name": "tiger",
        "health": 8,
        "strength": 5,
        "speed": 9,
        "drops": "raw meat"
    }
bear_lvl1 = {
        "name": "bear",
        "health": 14,
        "strength": 6,
        "speed": 4,
        "drops": "raw meat"
    }

# Conditional Functions
def game_over():
    print('Play again (Y / N)?')
    user_answer = input()
    if user_answer.lower() == "y":
        get_name(player)
    else:
        quit()

def get_random_enemy():
    enemies = [lion_lvl1, tiger_lvl1, bear_lvl1]
    random_enemy = random.choice(enemies)
    return random_enemy

def attack(attacker, defender):
    damage = random.randint(1, attacker["strength"])
    crit = random.randint(1, 10)
    if crit == 1:
        damage *= 1.5
        defender["health"] -= damage
        print(f"{attacker['name']} attacks, with a critical, and does {damage} damage.")
        print(f"{defender['name']} has {defender['health']} health left.")
    else:
        defender["health"] -= damage
        print(f"{attacker['name']} attacks and does {damage} damage.")
        print(f"{defender['name']} has {defender['health']} health left.")

def combat(player, enemy):
    if player["speed"] >= enemy["speed"]:
        first, second = player, enemy
    else: 
        first, second = enemy, player

    print(f"{first['name']} goes first.")

    while player["health"] > 0 and enemy["health"] > 0:
        attack(first, second)
        time.sleep(1)
        if second["health"] <=0:
            print(f"{first['name']} wins!")
            return first
        attack(second, first)
        time.sleep(1)
        if first["health"] <= 0:
            print(f"{second['name']} wins!")
            return second

# Gameplay Functions
def get_name(player):
    os.system("cls")
    player["name"] = input('What is your name? ')
    get_class(player)

def get_class(player):
    # Class info
    fighter = {
        "strength": 10,
        "speed": 5,
        "intelligence": 3,
        "health": 30,
    }

    assassin = {
        "strength": 5,
        "speed": 9,
        "intelligence": 7,
        "health": 15
    }

    mage = {
        "strength": 7,
        "speed": 6,
        "intelligence": 10,
        "health": 20
    }

    print("In this game, you can choose from 3 classes to start out as")
    #time.sleep(2)

    # Classes
    print("----------")
    print("Fighter")
    print(f"Strength: {fighter['strength']}")
    print(f"Speed: {fighter['speed']}")
    print(f"Intelligence: {fighter['intelligence']}")
    print(f"Health: {fighter['health']}")
    #time.sleep(3)

    print("----------")
    print("Assassin")
    print(f"Strength: {assassin['strength']}")
    print(f"Speed: {assassin['speed']}")
    print(f"Intelligence: {assassin['intelligence']}")
    print(f"Health: {assassin['health']}")
    #time.sleep(3)

    print("----------")
    print("Mage")
    print(f"Strength: {mage['strength']}")
    print(f"Speed: {mage['speed']}")
    print(f"Intelligence: {mage['intelligence']}")
    print(f"Health: {mage['health']}")
    #time.sleep(3)

    print("----------")
    print("Which class will you pick (F / A / M)?")
    user_answer = input()
    if user_answer.lower() == "f":
        fighter_class_chosen(player)
    elif user_answer.lower() == "a":
        assassin_class_chosen(player)
    elif user_answer.lower() == "m":
        mage_class_chosen(player)
    else:
        print("Invalid option...")
        #time.sleep(3)
        get_class(player)

def fighter_class_chosen(player):
    fighter = {
        "strength": 10,
        "speed": 5,
        "intelligence": 3,
        "health": 30,
    }
    os.system('cls')
    player["class"] = "fighter"
    player["strength"] = fighter["strength"]
    player["speed"] = fighter["speed"]
    player["intelligence"] = fighter["intelligence"]
    player["health"] = fighter["health"]
    print("Fighter class chosen!")
    #time.sleep(3)

    # Weapon
    print()
    print("You have the choice between 2 weapons...")
    print("The Greatsword (+5 Strength)")
    print("or")
    print("The Warhammer (+7 Strength / -3 Speed)")
    #time.sleep(3)

    print("Which weapon shall you pick (GS / WH)?")
    user_answer = input()
    if user_answer.lower() == "gs":
        greatsword_chosen(player)
    elif user_answer.lower() == "wh":
        warhammer_chosen(player)
    else:
        print("Invalid Option...")
        #time.sleep(3)
        fighter_class_chosen(player)

def greatsword_chosen(player):
    player["weapon"] = "greatsword"
    player["strength"] += 5
    print("Greatsword Chosen!")
    print("Beginning adventure now...")
    start_adventure(player)

def warhammer_chosen(player):
    player["weapon"] = "warhammer"
    player["strength"] += 7
    player["speed"] -= 3
    print("Warhammer Chosen!")
    print("Beginning adventure now...")
    start_adventure(player)

def assassin_class_chosen(player):
    assassin = {
        "strength": 5,
        "speed": 9,
        "intelligence": 7,
        "health": 15
    }
    os.system('cls')
    player["class"] = "asassin"
    player["strength"] = assassin["strength"]
    player["speed"] = assassin["speed"]
    player["intelligence"] = assassin["intelligence"]
    player["health"] = assassin["health"]
    print("Assassin class chosen!")
    #time.sleep(3)

    # Weapon
    print()
    print("You have the choice between 2 weapons...")
    print("The Daggers (+2 Speed)")
    print("or")
    print("The Longbow (+3 Strength / -2 Speed)")
    #time.sleep(3)

    print("Which weapon shall you pick (D / LB)?")
    user_answer = input()
    if user_answer.lower() == "d":
        daggers_chosen(player)
    elif user_answer.lower() == "lb":
        longbow_chosen(player)
    else:
        print("Invalid Option...")
        #time.sleep(3)
        assassin_class_chosen(player)

def daggers_chosen(player):
    player["weapon"] = "daggers"
    player["speed"] += 2
    print("Daggers Chosen!")
    print("Beginning adventure now...")
    start_adventure(player)

def longbow_chosen(player):
    player["weapon"] = "longbow"
    player["strength"] += 3
    player["speed"] -= 2
    print("Longbow Chosen!")
    print("Beginning adventure now...")
    start_adventure(player)

def mage_class_chosen(player):
    mage = {
        "strength": 7,
        "speed": 6,
        "intelligence": 10,
        "health": 20
    }
    os.system('cls')
    player["class"] = "mage"
    player["strength"] = mage["strength"]
    player["speed"] = mage["speed"]
    player["intelligence"] = mage["intelligence"]
    player["health"] = mage["health"]
    print("Mage class chosen!")
    #time.sleep(3)
    
    # Weapon
    print()
    print("You have the choice between 2 weapons...")
    print("The Spellbook (+3 Health / +2 Speed)")
    print("or")
    print("The Divine Staff (+5 Strength / -5 Health)")
    #time.sleep(3)

    print("Which weapon shall you pick (SB / DS)?")
    user_answer = input()
    if user_answer.lower() == "sb":
        spellbook_chosen(player)   
    elif user_answer.lower() == "ds":
        divine_staff_chosen(player)
    else:
        print("Invalid Option...")
        #time.sleep(3)
        mage_class_chosen(player)

def spellbook_chosen(player):
    player["weapon"] = "spellbook"
    player["health"] += 3
    player["speed"] += 2
    print("Spellbook Chosen!")
    print("Beginning adventure now...")
    start_adventure(player)

def divine_staff_chosen(player):
    player["weapon"] = "divine staff"
    player["strength"] += 5
    player["health"] -= 5
    print("Divine Staff Chosen!")
    print("Beginning adventure now...")
    start_adventure(player)

def start_adventure(player):
    os.system("cls")
    player["money"] = 100
    print(f"Welcome, {player['name']}!")
    print("You find yourself standing in the middle of a dirt road intersection.")
    print("You notice there is a pathway in all 4 directions")
    #time.sleep(3)

    print("Which path will you take (N, E, S, W)?")
    user_answer = input()
    if user_answer.lower() == "n":
        north_path(player)
    elif user_answer.lower() == "e":
        east_path(player)
    elif user_answer.lower() == "s":
        south_path(player)
    elif user_answer.lower() == "w":
        west_path(player)
    else:
        print("Invalid Option...")
        #time.sleep(2)
        start_adventure(player)

def north_path(player):
    os.system("cls")
    print("You take the north path...")
    print("You find that it leads you into a town, the name is unknown.")
    print("In the town there is a Bar, a Shop, and a Casino")
    #time.sleep(3)
    
    print("Where would you like to go (B / S / C)")
    user_answer = input()
    if user_answer.lower() == "b":
        go_to_bar(player)
    elif user_answer.lower() == "s":
        go_to_shop(player)
    elif user_answer.lower() == "c":
        go_to_casino(player)
    else:
        print("Invalid Option...")
        #time.sleep(3)
        north_path(player)

def go_to_bar(player):
    os.system("cls")
    print("You enter the bar...")

def go_to_shop(player):
    os.system("cls")
    print("You enter the shop...")

def go_to_casino(player):
    os.system("cls")
    print("You enter the shop to find it filled with games.")
    print("The one that catches your eye the most is the slot machines")
    print("Would you like to play (Y / N)?")
    user_answer = input()
    if user_answer.lower() == "y":
        slots.start_slot(player)
        leave_the_casino(player)
    elif user_answer.lower() == "n":
        back_to_town(player)
    else:
        print("Invalid Option...")
        go_to_casino(player)

def leave_the_casino(player):
    os.system("cls")
    print(f"You leave the casino with a total of {player['money']} coins.")
    print("As you are leaving, you pass a man standing in front of a door.")
    print("All you hear as you pass him is a faint, '100 coins and you can enter...'")
    print("You turn around to face him, but his face is expressionless.")
    print("You have two options")

    print()
    print("Will you Give him 100 Coins and test your luck")
    print("or")
    print("Leave the Casino")
    print("Which will you choose (GC / LC)?")
    user_answer = input()
    if user_answer.lower() == "gc":
        test_your_luck(player)
    elif user_answer.lower() == "lc":
        back_to_town(player)
    else:
        print("Invalid Option...")
        leave_the_casino(player)

def test_your_luck(player):
    if player["money"] < 100:
        print("The man realizes you don't have enough and FUCKING KILLS YOU")
        print("GAME OVER")
        print("----------")
        print("Enter to continue...")
        input()
        game_over()
    else:
        player["money"] -= 100
        print("You give the man 100 coins.")

def back_to_town(player):
    print("You decide to leave and go back to the town")
    print("Would you like to go to the Bar or Shop (B / S)?")
    user_answer = input()
    if user_answer.lower() == "b":
        go_to_bar(player)
    elif user_answer.lower() == "s":
        go_to_shop(player)
    else:
        print("Invalid Option...")
        back_to_town(player)

def east_path(player):
    enemy = get_random_enemy()
    os.system("cls")
    print("You wander down the path when you come upon some bushes.")
    print(f"From the bushes springs out a {enemy['name']} who looks hungry!")
    print("Will you fight or run?")
    #time.sleep(3)

    print("What will you choose (F / R)?")
    user_answer = input()
    if user_answer.lower() == "f":
        fight_1(player, enemy)
    elif user_answer.lower() == "r":
        run_1(player)
    else:
        print("Invalid Option...")
        #time.sleep(3)
        east_path(player)

def fight_1(player, enemy):
    os.system("cls")
    print("You choose to stand your ground... AND FIGHT!")
    winner = combat(player, enemy)
    if winner["name"] == player["name"]:
        print(f"You beat the {enemy['name']}!")
        print(f"Your remaining health is: {player['health']}.")
        print("----------")
        print("Enter to continue...")
        input()

        os.system("cls")
        print(f"After taking down the {enemy['name']} you loot its body.")
        print(f"+1 {enemy['drops']}")
        player["items"].append(enemy["drops"])
        print(player["items"])
    else:
        print('You lost to the lion on the east path......')
        print('GAME OVER')
        print("----------")
        print("Enter to continue...")
        input()
        game_over()

def run_1(player):
    os.system("cls")
    print("You turn tail and run straight back where you came from.")
    print("You return to where the other 3 paths are.")
    print("The remaining paths are West, North, and South")
    print("Which path will you choose (W / N / S)?")
    user_answer = input()
    if user_answer.lower() == "w":
        west_path(player)
    elif user_answer.lower() == "n":
        north_path(player)
    elif user_answer.lower() == "s":
        south_path(player)
    else:
        print("Invalid Option...")
        #time.sleep(2)
        run_1(player)

def south_path(player):
    os.system("cls")
    print("You take the south path...")
    print("For a while you don't find anything.")
    print("But just as you start to think its deserted, you come across a begger on the side of the road")
    print(f"'Please spare some change...' the man cries out.")
    print("Will you help the man or ignore his cries?")
    #time.sleep(2)

    print("What will you do (H / I)")
    user_answer = input()
    if user_answer.lower() == "h":
        help_the_man(player)
    elif user_answer.lower() == "i":
        ignore_the_man(player)
    else:
        print("Invalid Option...")
        #time.sleep(2)
        south_path(player)

def help_the_man(player):
    player["money"] -= 50
    print("-50 money")
    print(f"'Thank you, thank you!' the man exclaims.")
    print(f"'Please take this as a gift, I don't have much but I hope it's something!'")
    player["items"].append("rare jewel")
    print("+1 rare jewel")
    print(player)

def ignore_the_man(player):
    os.system("cls")
    print(f"'So that's how it is huh?!' the man exclaims.")
    print(f"'Fine then, I'll just take your stuff!'")
    print("You enter combat with the begger...")
    winner = combat(player, begger)
    if winner["name"] == player["name"]:
        print("You beat the begger!")
        print(f"Your remaining health is: {player['health']}.")
        print("----------")
        print("Enter to continue...")
        input()
    else:
        print("You lost to the begger on the south path......")
        print("GAME OVER")
        print("----------")
        print("Enter to continue...")
        input()
        game_over()

def west_path(player):
    os.system("cls")
    print("You take the west path...")

# Player Dictionary
player = {
    "name": "None",
    "strength": 0,
    "speed": 0,
    "intelligence": 0,
    "health": 0,
    "class": "None",
    "money": 0,
    "weapon": "None",
    "items": []
}
get_name(player)
