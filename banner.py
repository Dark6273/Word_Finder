# Import needed Library
import os # exit code
from colorama import Fore, init # colored text
from time import sleep # Time between two prints


init(autoreset=True)

# Main logo
def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.LIGHTCYAN_EX +"""
        ██╗    ██╗ ██████╗ ██████╗ ██████╗ 
        ██║    ██║██╔═══██╗██╔══██╗██╔══██╗
        ██║ █╗ ██║██║   ██║██████╔╝██║  ██║
        ██║███╗██║██║   ██║██╔══██╗██║  ██║
        ╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
        ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚════╝ 
          """)
    
# Menu options    
def menu():
    sleep(0.03)
    print(Fore.RED + ' [' + Fore.WHITE + '#' + Fore.RED + ']' + Fore.BLUE + " Choose one of the options below\n\n")
    sleep(0.03)
    print(Fore.YELLOW + ' [1] Word List')
    sleep(0.03)
    print(Fore.LIGHTMAGENTA_EX + ' [2] Add yes character')
    sleep(0.03)
    print(Fore.LIGHTRED_EX + ' [3] Add no character')
    sleep(0.03)
    print(Fore.LIGHTGREEN_EX + ' [4] Add character location')
    sleep(0.03)
    print(Fore.LIGHTMAGENTA_EX + ' [5] Remove yes character')
    sleep(0.03)
    print(Fore.LIGHTRED_EX + ' [6] Remove no character')
    sleep(0.03)
    print(Fore.LIGHTYELLOW_EX + ' [7] Print data')
    sleep(0.03)
    print(Fore.LIGHTRED_EX + ' [0] Exit...')

# Revice selection
def select():
    sleep(0.03) # 0.03s sleep
    try:
        # Print input text and turn it into number and return base
        return int(input(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + "WORD FINDER "+ Fore.GREEN +"<<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + "#" + Fore.RED +"] " + Fore.RESET))
    except:
        # In the event of incoming number
        return -1
    
# Get the number of word letters
def get_number():
    # Print main logo
    logo()
    try:
        # Get the number of the letters
        return int(input(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + "WORD FINDER "+ Fore.GREEN +"<<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + "?" + Fore.RED +"] " + Fore.YELLOW + 'How many letters is your word? ' + Fore.RESET))
    except:
        # Try again
        return int(input(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + "WORD FINDER "+ Fore.GREEN +"<<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + "?" + Fore.RED +"] " + Fore.YELLOW + 'How many letters is your word? ' + Fore.RESET))

# Get the status of the user to continue the program n => exit || other get => continue
def status():
    return input(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + "WORD FINDER "+ Fore.GREEN +"<<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + "?" + Fore.RED +"] " + Fore.YELLOW + 'Do you want to continue?('+ Fore.RED + 'n' + Fore.YELLOW + '/no || other/yes) ' + Fore.RESET)

# Add and remove characters to list
def character(text):
    return input(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + "WORD FINDER "+ Fore.GREEN + "~ " + Fore.BLUE + text + Fore.GREEN +"<<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + "?" + Fore.RED +"] " + Fore.YELLOW + 'Type the character you want ' + Fore.RESET)

# Print Good Bye :)
def bye():
    print(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + "WORD FINDER "+ Fore.GREEN +"<<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + "?" + Fore.RED +"] " + Fore.YELLOW + 'We hope you enjoy the app')

# Display word constraints
def data(yes, no, loc):
    print(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + "WORD FINDER "+ Fore.GREEN + "~ " + Fore.BLUE + "Data" + Fore.GREEN +"<<" + Fore.RED + "]\n |──╼ " + Fore.YELLOW + 'characters in the word ' + Fore.WHITE + yes + Fore.RED + "\n |──╼ " + Fore.YELLOW + 'characters not in the word ' + Fore.WHITE + no + Fore.RED + "\n └──╼ " + Fore.YELLOW + 'characters location in the word ' + Fore.WHITE + loc + Fore.RED)

# Get the position of letters
def location():
    try:
        # Trying to separate on :
        data = input(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + "WORD FINDER "+ Fore.GREEN + "~ " + Fore.BLUE + "Character location" + Fore.GREEN +" <<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + "?" + Fore.RED +"] " + Fore.YELLOW + 'Type the character location you want(example => 2:e) ' + Fore.RESET)
        data = data.split(":")
        return data
    except:
        # Wrong input
        return data[-1,-1]

# Call main menu 
def base():
    logo()
    menu()
    return select()
    
# Wrong Input
def wrong():
    print(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + "WORD FINDER "+ Fore.GREEN +"<<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + "?" + Fore.RED +"] " + Fore.YELLOW + 'The choice is wrong!!')