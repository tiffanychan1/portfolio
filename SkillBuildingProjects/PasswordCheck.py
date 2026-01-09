# Password parameter check

import re

print("A valid password contains a minimum of 6 characters, "
      "at least one number (0-9), letter (a-z), and special character($,#,@)")
print("Type your password and press Enter.")

# create custom exceptions
class TooShortError(ValueError):
    pass
class NoNumberError(ValueError):
    pass
class NoLetterError(ValueError):
    pass
class NoCharError(ValueError):
    pass

while True:
    try:
        # get user input
        password = input()
        
        # raise errors if parameters not met
        if len(password) < 6:
            raise TooShortError
        elif not re.search("[0-9]", password):
            raise NoNumberError
        elif not re.search("[a-z]", password):
            raise NoLetterError
        elif not re.search("[$#@]", password):
            raise NoCharError
        else:
            print("Your password is valid.")
            break
    
    # add messages for password improvement
    except TooShortError:
        print("Your password is too short, it must contain a minimum of 6 characters. Please try again.")
    except NoNumberError:
        print("Your password must contain a number. Please try again.")
    except NoLetterError:
        print("Your password must contain a letter. Please try again.")
    except NoCharError:
        print("Your password must contain a special character. Please try again.")
