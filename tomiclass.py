import random
import string
adjectives = ['sleepy','slow','smelly','tricky','orange']
nouns = ['apple','dino','tree','person','dummy']
print("WELCOME TO PASSWORD PICKER! :D")
def passwordGenrator():
    while True:
        adj = random.choice(adjectives)
        print("adjective  = ",adj)
        nn = random.choice(nouns)
        print("Noun: ",nn)
        number = random.randrange(1000, 10000)
        special_char = random.choice(string.punctuation)
        password = adj + nn + str(number) + special_char
            
        print("your new password is:",password)

            
        response = input('would you like more passwords? Type y or n:')
        if response =='n':
            break
passwordGenrator()
print("Tomi stopped/broke the loop")