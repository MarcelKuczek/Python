import random
import string

def random_char_generator(char_set ,count):
       return (random.choices(char_set,k = count))
       
def password_generator(lowercase_letters, uppercase_letters, special_signs, numbers):

        password.extend(random_char_generator(string.ascii_lowercase, lowercase_letters))
        password.extend(random_char_generator(string.ascii_uppercase, uppercase_letters))
        password.extend(random_char_generator(string.punctuation, special_signs))
        password.extend(random_char_generator(string.digits, numbers))
        
def shuffle_signs():
    random.shuffle(password)
    return(''.join(password)) 

password = []

lowercase_letters = int(input("How many lowercase letters: "))
uppercase_letters = int(input("How many upercase letters: "))
special_signs = int(input("How many special signs: "))
numbers = int(input("How many numbers: "))

password_generator(lowercase_letters, uppercase_letters, special_signs, numbers)
shuffle_signs()
print(password)
