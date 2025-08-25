#input

# income = input("Name: ");
# print("My name is ", income);

# age = input ("Tell me your age: ");
# print(f"I am {age} years old.");

#output is always str in input method;
#So, if we want an integer, we have to use int() method

num = input("Give a random number between 1 and 50: ");
print (type(num));  #str
print(type(int(num)));  #int