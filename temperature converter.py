print("choose the conversion you want to perform")
print("""1: Celcius to farenheit
2: farenheit to celcius """)
#get user input for conversion choice
choose=input("enter your choice 1 or 2")
#based on the user input we enter the respective conversion calculations
if choose=='1': #for the celcius to farenheit conversion
    celcius_input=float(input("enter the celcius"))
    farenheit = (9/5 * celcius_input) + 32
    print(f"{farenheit}F° is the temperature after converting the {celcius_input} c°")
elif choose=='2': #for the farenheit to celcius conversion
    farenheit_input=float(input("enter the farenheit"))
    celcius = (farenheit_input - 32) * (5/9)
    print(f"{celcius}C° is the temperature after converting {farenheit_input}F°")
else: #when user enters invalid input
    print("invalid input")