UserDict = {'name':'Rommuel', 'age': 21}

print(f"Original Dictionary: {UserDict}")

UserDict['City'] = "Manila"
print(f"Dictionary after adding new item (city:manila): {UserDict}")
UserDict['name'] = 'Rom'
print(f"Dictionary after updating an item (name): {UserDict}")
UserDict.pop('age')
print(f"Dictionary after deleting an item (age): {UserDict}")