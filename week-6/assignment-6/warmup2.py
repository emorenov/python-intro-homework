def celsius_to_fahrenheit(c):
    fahrenheit = c * (9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(f):
    celsius = (f - 32) * (5/9)
    return celsius

print(f'0\N{DEGREE SIGN}C = {celsius_to_fahrenheit(0):.1f}\N{DEGREE SIGN}F')
print(f'100\N{DEGREE SIGN}C = {celsius_to_fahrenheit(100):.1f}\N{DEGREE SIGN}F')
print(f'72\N{DEGREE SIGN}F = {fahrenheit_to_celsius(72):.1f}\N{DEGREE SIGN}C')