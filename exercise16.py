# Write a password generator in Python. Be creative with how you generate passwords 
# - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
#The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

# Extra:

# Ask the user how strong they want their password to be. 
# For weak passwords, pick a word or two from a list.
import random
listOfpass = ['moto','iphone','xiaomi','tesla','Elon','Musk','random']
strongList = ['a','b','c','A','B','C','z','Y','1','2','3','4','5','6','7','8','9','@','#','$']

def generatePassword(level):
    if level == 1:
        return random.sample(strongList,8)
    else:
        return random.sample(listOfpass,random.randint(1,2))


if __name__ == "__main__":
    strong = input("Enter 1 for Strong password, 2 for weak one: ")
    passw = generatePassword(int(strong))
    print("Tu password es: " + "".join(passw))