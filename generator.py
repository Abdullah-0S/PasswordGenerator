import random
from string import (
    ascii_uppercase as Uppercase ,
    ascii_lowercase as Lowercase,
    punctuation as Punctuation,
    digits as Digits,
    
) 
class generator:
    @staticmethod 
    def generate_password(uppercase : bool = True ,
                          lowercase : bool = True ,
                          punctuation : bool = True,
                          digits : bool = True,
                          length : int = 12,
                          minlength : int = 4,
                          maxlength : int = 128) -> str:
        # try:
        #     if length < 0 :
        #     raise new Exception 
        # catch:
        password : str = ""
        set_of_password = list() 
        if uppercase:
            set_of_password += list(Uppercase)
        if lowercase:
            set_of_password += list(Lowercase)
        if digits:
            set_of_password += list(Punctuation)
        if punctuation:
            set_of_password += list(Digits)
        for _ in range(length):
            password += random.choice(set_of_password)
        return password

def main() -> None:
    print(generator.generate_password())

if __name__ == "__main__":
    main()
