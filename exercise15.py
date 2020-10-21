# Write a program (using functions!) that asks the user for a long string containing multiple words. 
# Print back to the user the same string, except with the words in backwards order. 
# For example, say I type the string:

#   My name is Michele
# Then I would see the string:

#   Michele is name My
# shown back to me.

def reversed(s):
    list = s.split()
    return " ".join(list[::-1])

if __name__ == "__main__":
    s = input("Introduce una frase para mostrar en reversa: ")
    print(reversed(s))