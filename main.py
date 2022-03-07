# Import Mudels and banner
import mudels
import banner

# State Continue Ring => while Condintion
status = True

# while loop
while status:
    # Print the main menu and get input from the user
    select = banner.base()
    
    if select == 1: # select = 1 => List of words
        mudels.list_word()
        status = mudels.status(banner.status())
    
    elif select == 2: # select = 2 => Add letter in the word
        mudels.add_true_characters()
        status = mudels.status(banner.status())
    
    elif select == 3: # select = 3 => Add letter not in the word
        mudels.add_no_characters()
        status = mudels.status(banner.status())
        
    elif select == 4: # select = 4 => Add letter position
        mudels.add_character_location()
        status = mudels.status(banner.status())
        
    elif select == 5: # select = 5 => Deleting letters in the list (in the word)
        mudels.rm_yes_characters()
        status = mudels.status(banner.status())
        
    elif select == 6: # select = 6 => Deleting letters in the list (not in the word)
        mudels.rm_no_characters()
        status = mudels.status(banner.status())
        
    elif select == 7: # select = 7 => Data display
        mudels.data()
        status = mudels.status(banner.status())
        
    elif select == 0: # select = 8 => Exit the application
        mudels.bye()
        
    elif select == -1: # select = other => Wrong input
        mudels.wrong()
        status = mudels.status(banner.status())

# Exit the application
mudels.bye()