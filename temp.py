"""Temperature in degrees Fahrenheit (*F) = (Temperature in degrees Celcius (*C) * 9/5) + 32"""

"Convert temp from celcius to fahrenheit"
celcius = 25
convertToFahrenheit = (25* 9/5) + 32
print(f"{degrees} degrees is equal to {convertToFahrenheit:.0f} fahrenheit")

"""Funtion"""

def celcius_to_fahrenheit(celcius):
    """Convert celcius to fahrenheit"""
    fah = celcius * 9/5 + 32
    return fah

def fahrenheit_to_celcius(fahrenheit):
    """Convert fahrenheit to celcius"""
    celcius = fahrenheit - 32
    return celcius

fah = celcius_to_fahrenheit(celcius)
print(f"{celcius} degrees is {fah} Fahrenheit")

celcius = fahrenheit_to_celcius(fah)
print(f"{fah:.0f} Fahrenheit is {celcius} degress ")
