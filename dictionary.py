#Dictionary {key:value}
person = {
    "name":"kyawkyaw",
    "age" : 19
}

print(person["name"])
print(person["age"])

person["height"] = "165cm";

print(person);


#checking if the value is included in the dictionary

print ("name" in person)
print ("skin tone" in person)


#extracting keys/values as a list from a dictionary

print(list(person.keys()));
print(list(person.values()));

#looping a dictionary

person_items = person.items()

for (key,value) in person_items:
    print(f"{key}: {value}");

