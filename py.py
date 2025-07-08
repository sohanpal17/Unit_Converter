mass= {
    "kg": 1,
    "g" : 0.001,
    "mg" : 0.000001,
    "lbs" : 0.453592,
    'oz': 0.0283495,
    'ton': 1000
}
volume = {
    "l":1,
    "ml":0.001,
    'm3': 1000,
    'cm3': 0.001,
    'gallon': 3.78541,
    'pint': 0.473176
}
length = {
    "m": 1,
    'km': 1000,
    'cm': 0.01,
    'mm': 0.001,
    'mile': 1609.34,
    'inch': 0.0254,
    'ft': 0.3048,
    'yd': 0.9144,
}
speed = {
    'm/s': 1,
    'km/h': 0.277778,
    'mph': 0.44704,
    'ft/s': 0.3048,
    'knot': 0.514444
}
time = {
    "s": 1,
    "min": 60,
    "hr": 3600,
    "day": 86400,
    "ms": 0.001,
    "μs": 0.000001
}
area = {
    "m2": 1,
    "cm2": 0.0001,
    "mm2": 1e-6,
    "km2": 1e6,
    "ft2": 0.092903,
    "in2": 0.00064516,
    "acre": 4046.86,
    "hectare": 10000
    },
energy = {
    "joule": 1,
    "kJ": 1000,
    "cal": 4.184,
    "kcal": 4184,
    "wh": 3600,
    "kwh": 3.6e6
    },
power = {
    "watt": 1,
    "kW": 1000,
    "hp": 745.7,
    "mw": 0.001
    },
pressure = {
    "pa": 1,
    "kpa": 1000,
    "bar": 100000,
    "psi": 6894.76,
    "atm": 101325
    }
def unit_conversion():
    parameters =["Mass", "Volume", "Length", "Speed", "Time", "Area", "Energy", "Power", "Pressure"]
    print("Select the following conversion u need to do")
    for parameter in parameters:
        print(parameter)

    n=input().capitalize()
    if n=="Mass":
        keys = mass.keys()
        print("These are the following units")
        for k in keys:
            print(f"{k}")
        key= input().lower()
        if key in keys:
            i=input().lower()
            if i in keys:
                j=int(input())
                print(j*mass[key]/mass[i])
            else:
                print("The unit is not available")    
        else:
            print("The unit is not available")

    elif n=="Volume":
        keys = volume.keys()
        print("These are the following units")
        for k in keys:
            print(f"{k}")
        key= input().lower()
        if key in keys:
            i=input().lower()
            if i in keys:
                j=int(input())
                print(j*volume[key]/volume[i])
            else:
                print("The unit is not available")    
        else:
            print("The unit is not available")

    elif n=="Length":
        keys = length.keys()
        print("These are the following units")
        for k in keys:
            print(f"{k}") 
        key= input().lower()
        if key in keys:
            i=input().lower()
            if i in keys:
                j=int(input())
                print(j*length[key]/length[i])
            else:
                print("The unit is not available")    
        else:
            print("The unit is not available")
    elif n=="Speed":
        keys = speed.keys()
        print("These are the following units")
        for k in keys:
            print(f"{k}") 
        key= input().lower()
        if key in keys:
            i=input().lower()
            if i in keys:
                j=int(input())
                print(j*speed[key]/speed[i])
            else:
                print("The unit is not available")    
        else:
            print("The unit is not available")
    elif n=="Time":
        keys = time.keys()
        print("These are the following units")
        for k in keys:
            print(f"{k}") 
        key= input().lower()
        if key in keys:
            i=input().lower()
            if i in keys:
                j=int(input())
                print(j*time[key]/time[i])
            else:
                print("The unit is not available")    
        else:
            print("The unit is not available")
    elif n=="Area":
        keys = area.keys()
        print("These are the following units")
        for k in keys:
            print(f"{k}") 
        key= input().lower()
        if key in keys:
            i=input().lower()
            if i in keys:
                j=int(input())
                print(j*area[key]/area[i])
            else:
                print("The unit is not available")    
        else:
            print("The unit is not available")
         
    elif n=="Energy":
        keys = energy.keys()
        print("These are the following units")
        for k in keys:
            print(f"{k}") 
        key= input().lower()
        if key in keys:
            i=input().lower()
            if i in keys:
                j=int(input())
                print(j*energy[key]/energy[i])
            else:
                print("The unit is not available")    
        else:
            print("The unit is not available")
         
    elif n=="Power":
        keys = power.keys()
        print("These are the following units")
        for k in keys:
            print(f"{k}") 
        key= input().lower()
        if key in keys:
            i=input().lower()
            if i in keys:
                j=int(input())
                print(j*power[key]/power[i])
            else:
                print("The unit is not available")    
        else:
            print("The unit is not available")
    elif n=="Pressure":
        keys = pressure.keys()
        print("These are the following units")
        for k in keys:
            print(f"{k}") 
        key= input().lower()
        if key in keys:
            i=input().lower()
            if i in keys:
                j=int(input())
                print(j*pressure[key]/pressure[i])
            else:
                print("The unit is not available")    
        else:
            print("The unit is not available")    

    else :
        print("Not a valid conversion") 

while True:
    print("Welcome to Unit conversion program, Type ""Yes"" to continue and ""Exit"" to exit the program")
    again=input().lower()
    if again=="yes":
        unit_conversion()
    elif again=="exit":
        print("Program Exited Successfully.")
        break
    else:
        print("Not a valid answer")
