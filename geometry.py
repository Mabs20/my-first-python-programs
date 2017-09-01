# This program contains functions that evaluate formulas used in geometry.
#
# Marc Buena-Salas
# August 31, 2017

import math

def triangle_area(b, h):
    a = (1/2) * b * h
    return a

def circle_area(r):
    a = math.pi * r**2
    return a

def parallelogram_area(b, h):
    a = b * h
    return a

def trapezoid_area(a, b, h):
    a = (a + b) / 2 * h
    return a

def rectangular_prism_area(w, h, l):
    v = w * h * l
    return v

def cone_volume(r, h):
    v = math.pi * r**2 * h / 3
    return v

def sphere_volume(r):
    v = (4 / 3) * math.pi * r**3
    return v

def rectangular_prism_surface_area(w, h , l):
    sa = 2 * (( w * l ) + ( h * l ) + ( h * w ))
    return sa

def sphere_surface_area(r):
    sa = 4 * math.pi * r**2
    return sa

def hypotenuse_right_angle(a, b):
    c = ((a**2 + b**2)) ** (1 / 2)
    return c
# function calls
print(triangle_area(4,9))
print(circle_area(5))
print(circle_area(12))
print(parallelogram_area(3, 9))
print(trapezoid_area(4, 7, 2))
print(rectangular_prism_area(4, 9, 2))
print(cone_volume(2, 4))
print(sphere_volume(4))
print(rectangular_prism_surface_area(3, 6, 4))
print(sphere_surface_area(3))
print(hypotenuse_right_angle(4, 7))
