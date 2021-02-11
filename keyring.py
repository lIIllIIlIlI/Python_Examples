# Keyring is used to store passwords in your local keyring instead of hardcoding them in python.
# Passwords will be permanently installed in the keyring. Therefore, each password has to be 
# passed manually or via installation script.
# Keyring module will automatically detect the installed default keyring.

import keyring

# store password in keyring
keyring.set_password('twitter', 'myAccount', 'myPassword')

# retrieve password
keyring.get_password('twitter', 'myAccount')
