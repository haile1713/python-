names=[]
phone_numbers=[]


num=2

for j in range(num):
    name=input("enter name:")
    phone_number = int(input("enter phone number:"))

    names.append (name)
    phone_numbers.append (phone_number)

print("\t Name \t\t \t Phone number")

for i in range(num):
    print(f'\t {names[i]} \t\t\t {phone_numbers[i]}')

search=input("enter name :")

if search in  names:
    index=names.index(search)
    name=names[index]
    phone_number=phone_numbers[index]
    print(f'name:{name} phone number:{phone_number}')
else: 
    print("not found")
