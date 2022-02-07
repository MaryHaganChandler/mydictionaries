phonebook = {"Chris": "555−1111", "Katie": "555−2222", "Joanne": "555−3333"}


print()
print("*****  start section 1 - print dictionary ********")
print()

print(phonebook)

print(len(phonebook))

print(type(phonebook))

mydictionary = dict(
    m=8, n=9
)  # Can be any numbers or any letters; this just creates a dictionary (because of the "dict()" function)
print(mydictionary)

chris_phone = phonebook["Chris"]
print(chris_phone)

print()
print("*****  end section 1 ********")
print()


"""








print()
print("*****  start section 2 - search dictionary ********")
print()


name = "chris"

if name in phonebook:
    print(phonebook[name])
else:
    print("The name '" + name + "' is not found.")


print()
print("*****  end section 2 ********")
print()











print()
print("*****  start section 3 - edit/append dictionary ********")
print()


phonebook["Joe"] = "555-0123"
phonebook["Chris"] = "555-4444"

print(phonebook)

print()
print("*****  end section 3 ********")
print()











print()
print("*****  start section 4 - delete/remove from dictionary ********")
print()

del phonebook["Chris"]

print(phonebook)


print()
print("*****  end section 4 ********")
print()









print()
print("*****  start section 5 - iterate through keys ********")
print()

for key in phonebook:
    print(key)              #Iterates through the keys
    print(phonebook[key])   #Iterates through the values    Remember that "key" is just a variable!


print()
print("*****  end section 5 ********")
print()












print()
print('*****  start section 6 - iterate through values  ********')
print()



for value in phonebook.values():     #values is the method of the phonebook object
    #The word "value" is just a variable, but the method "values()" is a built-in method.
    print(value)





print()
print('*****  end section 6 ********')
print()












print()
print('*****  start section 7 - iterate through both key and value pair********')
print()

for phonebook_tuple in phonebook.items():
    #The items() method allows us to get both the key and the value at the same time.
    print(phonebook_tuple)
    print(type(phonebook_tuple))

for key, value in phonebook.items():
    print(key)
    print(value)


print()
print('*****  end section 7 ********')
print()












print()
print("*****  start section 8 - using get and clear methods********")
print()


phone = phonebook.get("Chris", "key not found")

print(phone)

phonebook.clear()

print(phonebook)


print()
print("*****  end section 8 ********")
print()











print()
print("*****  start section 9 - using pop and popitem methods********")
print()

# remove = phonebook.pop("Chris", "not found")

# print(remove)

# print(phonebook)





a = phonebook.popitem()

print(a)

print(phonebook)


print()
print("*****  end section 9 ********")
print()










import random

print()
print("*****  start section 10 - using random and converting to list   ********")
print()

# This basically does what popitem should do.

random_keys = list(phonebook)  #This creates a list from the dictionary. You need this to use random.choice.

print(random_keys)

choice = random.choice(random_keys)        ### random.choice is a function that only applies to lists

print(choice)

print(phonebook[choice])


#TO CONDENSE THE ABOVE LINES, you can just do two lines of code:
#choice = random.choice(list(phonebook))    
#print(phonebook[choice])
###OR
#random_phone = phonebook[random.choice(list(phonebook))]
#print(random_phone)

print()
print("*****  end section 10 ********")
print()








print()
print('*****  start section 11 - using random and converting to list ********')
print()




print()
print('*****  end section 11 ********')
print()

"""
