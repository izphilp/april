"""Temperature in degrees Fahrenheit (*F) = (Temperature in degrees Celcius (*C) * 9/5) + 32"""

"Convert temp from celcius to fahrenheit"
celcius = 25
Celtofah = (25* 9/5) + 32
print(f"{celcius} degrees is equal to {Celtofah:.0f} fahrenheit")

"""Funtion"""

def celcius_to_fahrenheit(celcius):
    """Convert celcius to fahrenheit"""
    fah = Celtofah
    return fah

def fahrenheit_to_celcius(fahrenheit):
    """Convert fahrenheit to celcius"""
    celcius = fahrenheit - 32
    return celcius

fah = celcius_to_fahrenheit(celcius)
print(f"{celcius} degrees is {fah:.0f} Fahrenheit")

celcius = fahrenheit_to_celcius(fah)
print(f"{fah:.0f} Fahrenheit is {celcius:.0f} degress ")
