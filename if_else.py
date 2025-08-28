#if else
age = int(input("Age: "))
if age >18 and age <30 :
    print("You are a young adult.");
elif age>18 :                            #else_if
    print("You are an adult.");
elif age>11 and age<18:                    #else
    print("You are an adolescent.");
else :
    print("You are a child.");