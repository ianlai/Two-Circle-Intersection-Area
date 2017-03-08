#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import math
import numpy as np
import sys

PI = 3.14159265359

### Default Setting 
x1 = 2.1
y1 = 1.8
r1 = 1.9

x2 = 5.3
y2 = 2.5
r2 = 3.2

numerical = False

def p(x):
    return pow(x,2)
def s(x):
    return pow(x,0.5)
def sin(x):
    return math.sin(x)
def cos(x):
    return math.cos(x)
def acos(x):
    return math.acos(x)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

class Circle:
    def __init__(self, r, p):
        self.r = r
        self.c = p
    def __str__(self):
        mystring = "radius=" + str(self.r) + ", center=" + str(self.c)
        return mystring
    def area(self):
        return str(PI*p(self.r))

def distance(p1,p2):
    return s(p(p1.x-p2.x)+p(p1.y-p2.y))

#target angle is between a and b
def cosine_rule(a,b,c):
    angle=acos((p(a)+p(b)-p(c))/(2*a*b))
    return angle

#theta is between a and b    
def triangle_area(a,b,theta):
    return 0.5*a*b*sin(theta)

def cone_area(r,theta):
    return p(r)*PI*theta/(2*PI)

if "--x1" in sys.argv:
    x1 = float(sys.argv[sys.argv.index("--x1")+1])
if "--y1" in sys.argv:
    y1 = float(sys.argv[sys.argv.index("--y1")+1])
if "--r1" in sys.argv:
    r1 = float(sys.argv[sys.argv.index("--r1")+1])
if "--x2" in sys.argv:
    x2 = float(sys.argv[sys.argv.index("--x2")+1])
if "--y2" in sys.argv:
    y2 = float(sys.argv[sys.argv.index("--y2")+1])
if "--r2" in sys.argv:
    r2 = float(sys.argv[sys.argv.index("--r2")+1])
if "-n" in sys.argv:
    numerical = True
if "--numerical" in sys.argv:
    numerical = True

p1 = Point(x1,y1)
p2 = Point(x2,y2)
c1 = Circle(r1,p1)
c2 = Circle(r2,p2)

if not numerical:
    print("=================================================================")
    print("Circle-1: " + str(c1) + " | Area=" + c1.area())
    print("Circle-2: " + str(c2) + " | Area=" + c2.area())
    print("=================================================================")

d = distance(c1.c, c2.c)
external_distance_bound = c1.r + c2.r
internal_distance_bound = math.fabs(c1.r - c2.r)

if d >= external_distance_bound:
    if not numerical:
        print("Two circles have no overlap.")
    else:
        print(0)
elif d <= internal_distance_bound:
    if not numerical:
        if r1 <= r2:
            print("Circle 1 is totally inside Circle 2.")
        else:
            print("Circle 2 is totally inside Circle 1.")
    else:
        if r1 <= r2:
            print(r1*r1*PI)
        else:
            print(r2*r2*PI)
else:
    theta1 = 2 * cosine_rule(c1.r, d, c2.r)
    theta2 = 2 * cosine_rule(c2.r, d, c1.r)

    t_area1 = triangle_area(c1.r, c1.r, theta1)
    c_area1 = cone_area(c1.r,theta1)
    t_area2 = triangle_area(c2.r,c2.r,theta2)
    c_area2 = cone_area(c2.r,theta2)

    two_circle_overlap_area = c_area1 + c_area2 - t_area1 - t_area2
    if not numerical:
        print("Overlap Area: " + str(two_circle_overlap_area))
    else:
        print(two_circle_overlap_area)
