from pathlib import Path
import json


path = Path('user_dict.json')

def user_and_info():
    """User inputs name and info about themselves and gets saved on a json file"""
    try:
        read = path.read_text()
        users_dict = json.loads(read)
        print('\nFile found\n')

    except(json.JSONDecodeError, FileNotFoundError):
        print('\nFile not found... Creating a new one\n')
        users_dict = {}

    while True:
        name = input("Type 'q' antime to quit\nWhat is your name? ").title()

        if name == 'Q': # changes for user exiting 
            print('\nGood day!')
            return None

        if not name.isalpha():
            print('Proper name please (letters only )')
            continue
        
        if len(name) <= 2:
            print('3 letter minimum please')
            continue

        running = True
        while running:
            if name in users_dict:
                while True:
                    again = input(f"\nare you sure you're {name}? Yes/No: ").lower()

                    if again == 'q': # changes for user exiting 
                        print('\nGood day!')
                        return None

                    if again == 'no':
                        print('\nRelogging...')
                        running = False
                        break

                    if again == 'yes':
                        break
                    
                    else:
                        print('Yes or No only please')
                        continue

                if not running:
                    break

                info = users_dict[name]
                print(f'\nWelcome back {name}! Your info below\n {name}: {info}')  # hashtagged code below is my original but inefficient code
                # for users, info in users_dict.items():
                #         if users == name:
                #             print(f'\nWelcome back {users}! Your info below\n {users}: {info}')
                
                while True:
                    again = input('\nWould you like to try logging-in again? Yes/No: ').lower()

                    if again == 'no':
                        print('\nGood day!')
                        return None

                    if again == 'yes':
                        running = False
                        break
                    
                    else:
                        print('Yes or No only please')
                        continue
                
                if running is False:
                    break
                
                continue
            
            else:
                break
        
        if not running:
            continue
        
        else:
            pass

        print(f'Saving name, {name}')
        
        information = input(f'A litte information about yourself {name}: ')
        users_dict[name] = information

        if information == 'q' or 'Q': # changes for user exiting 
                        print('\nGood day!')
                        return None

        while True:
            again = input('Would another person like to try? Yes/No: ').lower()

            if again == 'no':
                print('\nGood day!')
                path.write_text(json.dumps(users_dict))
                print('Current dictionary list:\n')
                for users, info in users_dict.items():
                    print(f'{users}: {info}')
                return users_dict
            
            if again == 'yes':
                break
            
            else:
                print('Yes or No only please')
                continue

user_and_info()       

#test test

    
    

    

    


    
    



