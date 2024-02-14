# test_temperature_converter.py
import temperature_converter
import math
def test_celsius_to_fahrenheit_to_celsius():
    celsius = 25
    fahrenheit = temperature_converter.celsius_to_fahrenheit(celsius)
    result = temperature_converter.fahrenheit_to_celsius(fahrenheit)
    assert result == celsius

def test_celsius_to_kelvin_to_celsius():
    celsius = 100
    kelvin = temperature_converter.celsius_to_kelvin(celsius)
    result = temperature_converter.kelvin_to_celsius(kelvin)
    assert result == celsius

def test_fahrenheit_to_kelvin_to_fahrenheit():
    fahrenheit = 32  # This is the freezing point of water in Fahrenheit
    kelvin = temperature_converter.fahrenheit_to_kelvin(fahrenheit)
    result = temperature_converter.kelvin_to_fahrenheit(kelvin)
    assert math.isclose(result, fahrenheit, rel_tol=1e-9)
