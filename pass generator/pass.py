import random 
import string

uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
numbers = string.digits
symbols = string.punctuation

print ("want a password? lets generate it for u ".upper())

num_uletters = int(input ("how many capital letters do u want ?\n"))
num_sletters = int(input ("how many small letters do u want ?\n"))
num_symbols = int(input ("how many symbols do u want ?\n"))
num_numbers = int(input ("how many numbers do u want ?\n"))


password =""

for j in range(1,num_uletters+1):
    char = random.choice(uppercase_letters)
    password += char
for j in range(1,num_sletters+1):
    char = random.choice(lowercase_letters)
    password += char
for j in range(1,num_symbols+1):
    char = random.choice(symbols)
    password += char
for j in range(1,num_numbers+1):
    char = random.choice(numbers)
    password += char

print (password)

