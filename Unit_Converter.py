Mass = {
    "kg": 1,
    "g" : 0.001,
    "mg" : 0.000001,
    "lbs" : 0.453592,
    'oz': 0.0283495,
    'ton': 1000
}
Volume = {
    "l":1,
    "ml":0.001,
    'm3': 1000,
    'cm3': 0.001,
    'gallon': 3.78541,
    'pint': 0.473176
}
Length = {
    "m": 1,
    'km': 1000,
    'cm': 0.01,
    'mm': 0.001,
    'mile': 1609.34,
    'inch': 0.0254,
    'ft': 0.3048,
    'yd': 0.9144,
}
Speed = {
    'm/s': 1,
    'km/h': 0.277778,
    'mph': 0.44704,
    'ft/s': 0.3048,
    'knot': 0.514444
}
Time = {
    "s": 1,
    "min": 60,
    "hr": 3600,
    "day": 86400,
    "ms": 0.001,
    "μs": 0.000001
}
Area = {
    "m2": 1,
    "cm2": 0.0001,
    "mm2": 1e-6,
    "km2": 1e6,
    "ft2": 0.092903,
    "in2": 0.00064516,
    "acre": 4046.86,
    "hectare": 10000
    }
Energy = {
    "joule": 1,
    "kJ": 1000,
    "cal": 4.184,
    "kcal": 4184,
    "wh": 3600,
    "kwh": 3.6e6
    }
Power = {
    "watt": 1,
    "kW": 1000,
    "hp": 745.7,
    "mw": 0.001
    }
Pressure = {
    "pa": 1,
    "kpa": 1000,
    "bar": 100000,
    "psi": 6894.76,
    "atm": 101325
    }
conversion_factors = {
    "a": "Mass",
    "b": "Volume",
    "c": "Length",
    "d": "Speed",
    "e": "Time",
    "f": "Area",
    "g": "Energy",
    "h": "Power",
    "i": "Pressure"
}
label ={
    "Mass" : Mass,
    "Volume" : Volume,
    "Length" : Length,
    "Speed" : Speed,
    "Time" : Time,
    "Area" : Area,
    "Energy" : Energy,
    "Power" : Power,
    "Pressure" : Pressure
}
def unit_conversion():
    parameters = conversion_factors.keys()
    print("Select the conversion you would like to perform by inputting its assigned letter.")
    for parameter in parameters:
        print(f"{parameter}) {conversion_factors.get(parameter)}")
    print("j) Temperature")

    conversion_type=input().lower()

    if conversion_type=="j":
        print("These are the following units")
        print("1) C\n"+ "2) F\n"+ "3) K\n")
        unit_input=input("Enter the unit to convert from (C/F/K): ").capitalize()
        

        if unit_input=="C":
            try:
                unit=float(input("Enter the value you want to convert: "))
                print(f"{unit*9/5+32:.2f} F")
                print(f"{unit+273.15:.2f} K")
            except ValueError:
                print("Enter only numbers")  
        elif unit_input=="F":
            try:
                unit=float(input())
                print(f"{(unit-32)*5/9:.2f} C")
                print(f"{(unit-32)*5/9+273.15:.2f} K")
            except ValueError:
                print("Enter only numbers")
        elif unit_input=="K":
            try:
                unit=float(input())
                print(f"{(unit-273.15)*9/5+32:.2f} F")
                print(f"{unit-273.15:.2f} C")
            except ValueError:
                print("Please enter a valid numeric input.")
        else:
            print("Invalid temperature unit.")        
            

    elif conversion_type in conversion_factors.keys():
        conversion_name=conversion_factors.get(conversion_type)
        master_dict=label.get(conversion_name)
        keys = master_dict.keys()
        print("\nAvailable units:\n")
        count=0
        for units in keys:
            count+=1
            print(f"{count}) {units}")
        unit1= input("\nConvert from: ").lower()
        if unit1 in keys:
            unit2=input("Convert to: ").lower()
            if unit2 in keys:

                try:
                    value =float(input("Enter the value to convert: "))
                    answer=value*master_dict[unit1]/master_dict[unit2]
                    print(f"{answer:.2f} {unit2}")
                    
                except ValueError:
                    print("Please enter a valid numeric value.")
                 
                     
            else:
                print("The inputted unit is invalid")    
        else:
            print("The inputted unit is invalid")
    else:
        print("Invalid selection. Please enter a valid letter from the list.")


while True:
    again = input( "Unit Conversion Program initialized. Enter 'Y' to continue or 'N' to close the application: ").capitalize()
    
    if again == "Y":
        unit_conversion()
          
    elif again == "N":
        print("Program exited successfully.")
        break
    else:
        print("Invalid response. Please enter 'Y' or 'N'.")       

  
