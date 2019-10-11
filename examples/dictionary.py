phonebook = {}

phonebook["Jack"] = 938477566
phonebook["John"] = 938477562
phonebook["Jill"] = 938477512

print(phonebook)

del phonebook["Jack"]

print(phonebook)

phonebook["Jake"] = 938273443
del phonebook["Jill"]

if "Jake" in phonebook:
    print("Jake is listed in the phonebook")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")