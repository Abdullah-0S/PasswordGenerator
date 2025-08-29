import random
from string import (
    ascii_uppercase as Uppercase ,
    ascii_lowercase as Lowercase,
    punctuation as Punctuation,
    digits as Digits,
    
) 
class generator:
    @staticmethod 
    def generate_password(
                          uppercase : bool = True , 
                          lowercase : bool = True ,
                          punctuation : bool = True,
                          digits : bool = True,
                          length : int = 12,
                          minlength : int = 4,
                          maxlength : int = 128,
                          block : set[str] = set() 
                          ) -> str:

        password : str = ""
        set_of_password : set[str] = set() 
        
        # adding possible set of password
        if uppercase:
            set_of_password |= set(Uppercase)
        if lowercase:
            set_of_password |= set(Lowercase)
        if digits:
            set_of_password |= set(Punctuation)
        if punctuation:
            set_of_password |= set(Digits)
        
        set_of_password -= block # remove the blocked text
        
        set_of_password = tuple(set_of_password) 
        
        # making the password randomly 
        for _ in range(length):
            password += random.choice(set_of_password)
        
        return password

def main() -> None:
    print()
    print()
    print()
    for _ in range(10):
        print("--> ",end="")
        print(generator.generate_password(block={*Punctuation}))
        print()

if __name__ == "__main__":
    main()
