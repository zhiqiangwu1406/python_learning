greet = "hello world";

# index

greet[0] #h
greet[10] #d
greet[-1] #d
print(greet[-11]) #h

#string slice method [inclusive:exclusive]

greet[2:8] #llo w
print(greet[3:-2] )#lo wor

#string concatenation

str1 = "hel"
str2 = "lo"
resultStr = str1 + str2  #hello
print(resultStr)

str3= "hi"
print(str3*3)   #hihihi

#some methods for changing cases



upperCaseGreet = greet.upper() #HELLO WORLD
print(upperCaseGreet);

#split method

names = "aungaung,susu,mgmyo";
print (names.split(","))  #["aungaung","susu","mgmyo"]   (list data type)

#length of string
print (len(greet)) #11