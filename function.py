def greet():
    print("Hello World!!");

greet();

def greeting(name, time):
    print(f"Good {time}, {name}");

name=input("Name: ");
time= input("time: ");
greeting(name,time);

#default parameter 
def greeting2(name="aungaung", time="night"):  #use the default one when no parameter is added while calling
    print(f"Good {time}, {name}");
greeting2();