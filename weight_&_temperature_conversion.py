#Python weight converter
print("\033[1;41m***Welcome to weight conversion program*****\033[0m\n")
# 👆 printing in bold (1m) and highlighting with red(41m) in python
weight=float(input("Enter your weight: "))
unit = input(" The weight is in Kilograms or Pounds (KG or LBS) ")
unit=unit.replace(" ","").upper()
if unit in ("KGS","KG","KILO","KILOGRAMS","K"):
    weight*=2.205
    unit = " Lbs."
elif unit in ("LBS","LB","POUND","POUNDS","L"):
    weight/=2.205
    unit="Kgs."
else:
    print(f"{unit} was not valid ")

print(f"\033[43mYour weight is {round(weight,2)} {unit} \033[0m")

#Python temperature converter
print("\n\033[1;41m***Welcome to temperature conversion program*****\033[0m\n")
unit2=input("Enter your unit of temperature Celsius(C) or Fahrenheit(F) or Kelvin(K)) ").upper().replace(" ","")
T=float(input("Enter the temperature "))
convert_to= input("And you want to convert the temperature in Celsius(C) or Fahrenheit(F) or Kelvin(K)) ").upper().replace(" ","")
if unit2 =='C':
    if convert_to == "F":
        temp=(9/5*T)+32
        u="°F"

    elif convert_to =="K":
        temp=(273.15+T)
        u = "K"
    elif convert_to == "C":
        temp = T  # No conversion needed, same unit
        u = "°C"
    else:
        temp = None
        print("Invalid unit")
elif unit2=='F':
    if convert_to == "C":
        temp=(5/9*T)-32
        u = "°C"
    elif convert_to =="K":
        temp=((5/9*T)-32+273.15)
        u = "K"
    elif convert_to == "F":
        temp = T
        u = "°F"
    else:
        temp=None
        print("Invalid unit")
elif unit2=='K':
    if convert_to == "C":
        temp=T-273.15
        u = "°C"
    elif convert_to =="F":
        temp=(9/5*(T-273.15))+32
        u = "°F"
    elif convert_to == "K":
        temp = T
        u = "K"
    else:
        temp = None
        print("Invalid unit")
else:
    print("Please enter a correct input")
print(f"\033[42m The converted temperature is {temp:.3f} {u} \033[0m")




