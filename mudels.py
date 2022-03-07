# import the required libraries
import banner
from time import sleep
from sys import exit
from colorama import Fore

# Difine variables
FREQ = 'esiarntolcdugpmkhbyfvwzxqj' # Arrange on the basis of the more use
yes_char = list()
no_char = list()
char_loc = dict()

# Open the file and read data with in
with open('words') as f:
    words = f.readlines()
    
# Isolation of the words based on number if letters
def split_word(words, count):
    ls = list()
    words = [ word.strip() for word in words ] # Delete \n from end of word
    for word in words:
        if len(word) == count:
            ls.append(word)
    return ls

# Function call 
words = split_word(words, banner.get_number())

# Display alphabetic sorting words
def list_word():
    # Scrolling over all the words
    for word in words:
        # Define needed variables
        score = 0
        count_yes_char = 0
        count_no_char = 0
        count_loc = 0
        
        # Counting letters
        for character in set(list(word)):
            if character in no_char:
                count_no_char += 1
                
            elif character in yes_char:
                count_yes_char += 1
            score += FREQ.index(character)
                
        # Checks based on letters
        if count_no_char == 0 and count_yes_char >= len(yes_char):
            ls_char = list(word)
            keys = char_loc.keys()
            
            # Checks based on letters position
            for key in keys:
                if ls_char[int(key) - 1] == char_loc[key]:
                    count_loc += 1
            if len(keys) == count_loc:
                print(word, Fore.RED + str(score), Fore.RESET)
   
# Add letters in the word
def add_true_characters():
    characters = banner.character("Add characters in the word").lower()
    for character in characters:
        if character not in yes_char: # Added if there are no in the list
            yes_char.append(character)
            
# Add letters not in the word
def add_no_characters():
    characters = banner.character("Add characters not in the word").lower()
    for character in characters:
        if character not in no_char: # Added if there are no in the list
            no_char.append(character)

# Add letters place
def add_character_location():
    data = banner.location()
    
    # Wrong data
    if data[0] == -1:
        wrong()
    else:
        try:
            # Add letter in the dictionary and postions
            char_loc[int(data[0])] = data[1]
            if data[1] not in yes_char: # Added if there are no in the list
                yes_char.append(data[1])
        except:
            # Wrong data
            wrong()
   
# Remove letters from the list
def rm_yes_characters():
    characters = banner.character("remove characters in the word").lower()
    for character in characters:
        if character in yes_char:
            yes_char.remove(character)
    
# Remove letters from the list
def rm_no_characters():
    characters = banner.character("remove characters not in the word").lower()
    for character in characters:
        if character in no_char:
            no_char.remove(character)

# Preparation of Data to print and send it
def data():
    yes = ''
    no = ''
    loc = ''
    
    for character in yes_char:
        yes += character + ' '
        
    for character in no_char:
        no += character + ' '
        
    keys = char_loc.keys()
    
    for key in keys:
        loc += char_loc[key] + ": " + str(key) +' '
        
    banner.data(yes, no, loc)
    
# Checking the situation  
def status(status):
    if status == 'n':
        return False
    else:
        return True
   
# Exit the application
def bye():
    sleep(0.3)
    banner.bye()
    sleep(0.3)
    exit()
    
# Wrong input or data
def wrong():
    sleep(0.3)
    banner.wrong()
    sleep(1)
