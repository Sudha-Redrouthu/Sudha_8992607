# test_geometry_calculator.py
import Formulasforshapes
import math
def test_area_circle():
    radius = 5
    expected_area = math.pi * radius * radius
    calculated_area = Formulasforshapes.area_circle(radius)
    assert calculated_area == expected_area

def test_area_rectangle():
    length, width = 10, 20
    expected_area = length * width
    calculated_area = Formulasforshapes.area_rectangle(length, width)
    assert calculated_area == expected_area
