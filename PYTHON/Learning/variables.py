# variable= A containes for a value which is used to store data in a program.()string,integer,float,boolean)    
# f string is used to format the string.

# STRING

first_name="Anshika"
food="Pizza"
fav_country="Japan"
watch="Animes"
print(first_name)
print(f"Hey my name is {first_name}")
print(f"my favourite food is {food}")
print(f"Want to go to {fav_country}")
print(f"I love watching {watch}")

# INTEGER

age=20
at_age= 25

print(f"I am {age} years old and want to work in japan at the age of {at_age}.")

# FLOAT

price= 99.99
cgpa= 8.7
Population= 2.3
print(f"Yesterday i bought a T-Shirt of price ${price}. I got {cgpa} cgpa in my 1st year. i live in a country which has {Population} population.")

# BOOLEAN (TRUE/FALSE)

is_student = True
for_sale = False

print(f"Are you a student?: {is_student}")

if is_student:
    print("You are a student")
else:
    print("You are not a student")

if for_sale:
    print("That item is FOR SALE!!!")
else:
    print("That item is NOT Available..")