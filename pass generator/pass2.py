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


pass_list =[]

for j in range(1,num_uletters+1):
    char = random.choice(uppercase_letters)
    pass_list += char
for j in range(1,num_sletters+1):
    char = random.choice(lowercase_letters)
    pass_list += char
for j in range(1,num_symbols+1):
    char = random.choice(symbols)
    pass_list += char
for j in range(1,num_numbers+1):
    char = random.choice(numbers)
    pass_list += char

random.shuffle (pass_list)
password =""
for i in pass_list:
     password += i

print (password)




