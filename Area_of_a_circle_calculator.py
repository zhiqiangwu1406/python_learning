#Area of a circle calculator

# radius = int(input("Radius (in cm) :" ));


inputValue = input("Radius (in cm) :" );
if inputValue.__contains__("."):
    radius = float(inputValue);
else :
    radius = int(inputValue);
pi = 3.142;
Area = round(pi*(radius**2), 3);
print (f"The area of the circle is {Area} cm\u00b2");

