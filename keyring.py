# Keyring is used to store passwords in your local keyring instead of hardcoding them in python.
# Passwords will be permanently installed in the keyring. Therefore, each password has to be 
# passed manually or via installation script.
# Keyring module will automatically detect the installed default keyring.

import keyring
import getpass 

# retrieve password
twitterPassword = keyring.get_password('twitter', 'twitterAccount')

if not twitterPassword:
  twitterPassword = getpass.getpass(prompt='Enter your twitter password') 
  # store password in keyring
  keyring.set_password('twitter', 'twitterAccount', 'twitterPassword')

print(twitterPassword)

