def clear_screen(): 
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')
    print('    ')

print('Start?')
print('    ')

player_name = ""
Class = 0

def Check():
    if Class == 1:
        print(f'You are a Mage named {player_name}. You have a wand and a tome. Your Max Hp is 4, Your current Hp is 4.')
    elif Class == 2: 
        print(f'You are a Warrior named {player_name}. You have a shield and a short sword. Your Max Hp is 6, Your current Hp is 6.')
    elif Class == 3:
        print(f'You are a Druid named {player_name}. You have a pouch of herbs and a staff. Your Max Hp is 5, Your current Hp is 5.')
    else:
        print("Your class is not set yet.")

def choose_option(prompt, options):
    print(prompt)
    for key, value in options.items():
        print(f"{key}: {value}")
    while True:
        choice = input("Choose one option. ").strip().upper()
        if choice in options:
            return choice
        else:
            print("Please type A, B, or C.")

def start_game():
    global player_name, Class
    print('Welcome traveler. Please, tell me what I may call you.')
    print('    ')
    player_name = input('Enter your name: ')
    print('    ')
    print(f'It is a pleasure, {player_name}. I am glad we made this connection')
    print('    ')
    print('I have a few more questions for you, if you would be so kind as to answer them.')
    print('    ')
    print('I want to know what it is you yearn for.')
    print('    ')
    options = {
        'A': 'Mezmorized by Magic',
        'B': 'Mezmorized by War',
        'C': 'Mezmorized by Earth'
    }
    choice = choose_option("What is it you are mezmorized by?", options)
    print(f'You chose: {options[choice]}')
    print('    ')
    if choice == 'A':
        Class = 1
        print('The light of the arcane shines bright in you, a good choice.')
    elif choice == 'B':
        Class = 2
        print('The adrenaline of fight pumps within, a good choice indeed.')
    elif choice == 'C':
        Class = 3
        print('The ground you walk is worthy, a good choice.')
    print('    ')
    if Class == 1:
        print('You feel a small wooden wand resting in your palm, and a tome resting on a sash around your shoulder')
    if Class == 2:
        print('You feel a shield resting around your arm, and a short sword on your hip')
    if Class == 3:
        print('You feel a small pouch of various herbs, and a staff on your back')
    print('    ')
    print('One last thing, if you ever need, just type "Check" and you may view your condition')
    print('    ')
    print('Now, shall we begin?')
    options = {
        'Y' : 'Yes',
        'N': 'No'
        }
    choice = choose_option("   ", options)
    print(f'You chose: {options[choice]}')
    print('    ')

    if choice == 'Y':

        print('Excellent! Let us begin!')
        clear_screen() 
    elif choice == 'N':
        print('Unfortunate, let us begin anyway!')

        clear_screen()  
    if choice == 'Y':

        print('Excellent! Let us begin!')
       
    elif choice == 'N':
        print('Unfortunate, let us begin anyway!')

       

def game_loop():
    while True:
        command = input('     ').strip().lower()
        if command == "check":
            Check()
        elif command in ["quit", "exit"]:
            print("     ")
            break
        else:
            print(f'You typed: {command} (but nothing happened)')

def swait():
    input(' Press enter to continue')
    print('    ')
    start_game()
    game_loop()

swait()