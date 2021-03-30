print("Solutions for IC problems")

print("Select the required number")
print("1. Inverting")
print("2. Non inverting")
print("3. Voltage adder")
print("4. Voltage substracter")

required == int(input("Enter the number =  "))
if required == 1:
    print("Enter the following values")
    Vi = int(input("Enter the input voltage =  "))
    Rf = int(input("Enter the feedback resistance = "))
    R1 = int(input("Enter the series resistance = "))
    print(f"('Output voltage = -{Rf}/{R1}*{Vi}')")
elif required == 2:
    print("Enter the following values")
    Vi = int(input("Enter the input voltage =  "))
    Rf = int(input("Enter the feedback resistance = "))
    R1 = int(input("Enter the series resistance = "))
    print(f"('Output voltage = [1+[{Rf}/{R1}]]*{V1}')")
elif required == 3:
     print("Enter the following values")
     V1 = int(input("Enter the first input voltage = "))
     V2 = int(input("Enter the second input voltage"))
     print(f"('The output voltage = {V1}+{V2}')")
elif required == 4:
     print("Enter the following values")
     V1 = int(input("Enter the positve input voltage = "))
     V2 = int(input("Enter the negative input voltage = "))
     print(f"('The output voltage = {V1}-{V2}')")
     
else:
    print("Error")    
     

    