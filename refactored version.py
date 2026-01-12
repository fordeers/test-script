from pathlib import Path
import json


path = Path('user_dict.json')

def json_try(path):
    try:
        read = path.read_text()
        users_dict = json.loads(read)
        print('\nFile found\n')
        return users_dict

    except(json.JSONDecodeError, FileNotFoundError):
        print('\nFile not found... Creating a new one\n')
        users_dict = {}
        return users_dict

def asks_name():
    while True:    
        name = input("\nType 'end' anytime to quit\nWhat is your name? ").title()

        if name == 'End': # changes for user exiting 
            print('\nGood day!')
            return 'end'

        if not name.isalpha():
            print('\nProper name please (letters only)')
            continue
        
        if len(name) <= 2:
            print('\n3 letter minimum please')
            continue
        
        return name
            
def verify_user(name, dict):
    if name in dict:
        while True:
            again = input(f"\nare you sure you're {name}? Yes/No: ").lower()

            if again == 'end': # changes for user exiting 
                print('\nGood day!')
                return 'end'

            if again == 'no':
                print('\nRelogging...')
                return 'relog'

            if again == 'yes':
                break
            
            else:
                print('Yes or No only please')
                continue

        info = dict[name]
        print(f'\nWelcome back {name}! Your info below\n {name}: {info}')  # hashtagged code below is my original but inefficient code
        # for users, info in users_dict.items():
        #         if users == name:
        #             print(f'\nWelcome back {users}! Your info below\n {users}: {info}')
        
        while True:
            again = input('\nWould you like to try logging-in again? Yes/No: ').lower()

            if again == 'no':
                print('\nGood day!')
                return 'end'

            if again == 'yes':
                return 'relog'
            
            else:
                print('Yes or No only please')
                continue
        
def saving_info(dict):
    path.write_text(json.dumps(dict))
    print('Current dictionary list:\n')
    for users, info in dict.items():
        print(f'\t{users}: {info}')

def next_person():
    while True:
            again = input('\nWould another person like to try? Yes/No: ').lower()

            if again == 'no':
                print('\nGood day!')
                return 'end'
            
            if again == 'yes':
                return 'relog'
            
            else:
                print('Yes or No only please')
                continue

def get_info(name, dict):
    information = input(f'A litte information about yourself {name}: ')

    if information == 'end': # changes for user exiting 
        print('\nGood day!')
        return 'end'
    
    dict[name] = information
    saving_info(dict)

def user_and_info():
    """User inputs name and info about themselves and gets saved on a json file"""
    
    user_dict = json_try(path)

    while True:
        
        name = asks_name()
        if name == 'end':
            return None

        verify = verify_user(name, user_dict)
        if verify == 'end':
            return None
        
        if verify == 'relog':
            continue

        print(f'Saving name, {name}')
        
        info = get_info(name, user_dict)
        if info == 'end':
            return None

        pass_along = next_person()
        if pass_along == 'end':
            saved_info = saving_info(user_dict)
            return saved_info   
             
        if pass_along == 'relog':
            continue

user_and_info()