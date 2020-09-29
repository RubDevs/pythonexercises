# Ask user for a word and return a message either the word is a palindrome or not

word = input("Escribe una palabra: ")
new = word[-1::-1]
print("Es palindromo") if word == new else print("No es palindormo")
