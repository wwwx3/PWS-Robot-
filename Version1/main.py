#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from math import atan2, degrees, sqrt
#from turtle import speed, pensize, pendown, left, forward


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
right_motor = Motor(Port.C)
left_motor = Motor(Port.B)
gyro = GyroSensor(Port.S3, Direction.CLOCKWISE)
cutter_equipped = True
if cutter_equipped == True:
    motor1 = Motor(Port.D)
    motor2 = Motor(Port.A)

robot = DriveBase(left_motor, right_motor, wheel_diameter = 56, axle_track = 110)
cutter = 0 #the leave cutter motor 
current_x = 0
current_y = 0
current_angle = 0
unit = 10 #mm per unit

"""input points[]"""

#ggearthy points = [(0.0, 0.0), (0.0, 214.4358555270136), (279.1832048270756, 217.6809844882485), (259.35487773870204, 42.0651264766684)]
#ggearth2y points = [(0.0, -0.0), (0.0, 305.6189289130089), (75.94102276679222, 325.8207048937061), (255.82097614570586, 186.27367112376214), (257.093483089354, 58.15956789673297)]   
#squre points = [(0,0),(0,120),(120,120),(120,0)]
#pentagon points = [(0,0),(70,0),(120,60),(120,120),(70,180),(0,180)]
#Trapezoid points = [(0,0),(0,160),(120,90),(120,0)]
#Octagon points = [(40,0),(70,0),(120,50),(120,110),(60,180),(30,180),(0,150),(0,30)]
#demo 
points = [(0,0),(60,0),(90,20),(60,60),(90,120),(0,120),(20,60)]

line_spacing = 20 #in unit
accumulate_error = 6 #mm

#variable for pid control
error = 0
integral = 0
derivative = 0
last_error = 0
kp = 4.5
ki = 0
kd = 0.6

"""
speed(1)
pensize(2)
pendown()
"""
def press_start():
    ev3.screen.print("Press to start")
    while not Button.CENTER in ev3.buttons.pressed():
        pass 
    ev3.screen.clear()

def brake():
    robot.stop()
    right_motor.brake()
    left_motor.brake()


def track_gyro():
    while robot.distance() < 900:
        robot.drive(100,gyro.angle()*-4) 

def move(distance = 0, speed = 0):
    """Move the robot forward or backward by a specific distance in centimeters."""
    while robot.distance() < distance:
        robot.drive(speed,0)
    brake()
    robot.reset()

def track_gyro_pid(distance = 0, speed = 0, target = 0):
    global error, last_error, integral, derivative, kp, ki, kd
    while robot.distance() < distance:
        error = target - gyro.angle()
        integral = integral + error
        derivative = error - last_error
        turn_rate = (error*kp)+(integral*ki)+(derivative*kd)
        robot.drive(speed,turn_rate)
        last_error = error
    brake()
    robot.reset()


def turn(turn_angle = 0, speed = 0):
    """Turn the robot by a specific angle in degrees."""
    
    if gyro.angle() < (turn_angle - current_angle):
        while gyro.angle() < (turn_angle - current_angle): 
            robot.drive(0, speed)
    elif gyro.angle() > (turn_angle - current_angle):
        while gyro.angle() > (turn_angle - current_angle):
            robot.drive(0, -speed)
    else:
        pass
    brake()


def goto(target_x,target_y): 
    
    global current_x, current_y, current_angle
   
    dx = target_x - current_x
    dy = target_y - current_y
    distance = sqrt(dx**2 + dy**2)
    distance = (distance*unit) + accumulate_error
    target_angle = degrees(atan2(dy, dx))

    turn_angle = target_angle - current_angle
    if turn_angle > 180:
        turn_angle = -1*(360 - turn_angle)
    if turn_angle < -180:
        turn_angle = -1*(-360 - turn_angle)
    
    turn_angle = -turn_angle #gyro sensor clockwise = positive while in xy plane counterclockwise = positive 
    
    if cutter == 1:
        turn(turn_angle, 100)
        cutter_on()
        track_gyro_pid(distance, 200, -target_angle)
        cutter_off()
    else:
        turn(turn_angle, 100)
        track_gyro_pid(distance, 200, -target_angle)

    current_x = target_x
    current_y = target_y
    current_angle = target_angle

def draw_field(points):
    goto(points[0][0], points[0][1])
    for point in points:
        goto(point[0], point[1])
    goto(points[0][0], points[0][1])
    # Close the polygon

def is_point_in_field(x, y, points):
    """Check if a point is inside a polygon using the ray-casting algorithm."""
    num = len(points)
    j = num - 1
    inside = False
    for i in range(num):
        if ((points[i][1] > y) != (points[j][1] > y)) and \
                (x < points[i][0] + (points[j][0] - points[i][0]) * (y - points[i][1]) / (points[j][1] - points[i][1])):
            inside = not inside
        j = i
    return inside

#horizontal line
def draw_zigzag_lines_x(points, line_spacing):
    global cutter
    min_x = int(min(point[0] for point in points))
    max_x = int(max(point[0] for point in points))
    min_y = int(min(point[1] for point in points))
    max_y = int(max(point[1] for point in points))

    direction = 1
    for y in range(min_y, max_y, int(line_spacing)):
        line_points = []
        for x in range(min_x, max_x):
            if is_point_in_field(x, y, points):
                line_points.append((x, y))

        if line_points:
            if direction == 1:
                goto(line_points[0][0], y)
                cutter = 1
                goto(line_points[-1][0], y)
                cutter = 0
            else:
                goto(line_points[-1][0], y)
                cutter = 1
                goto(line_points[0][0], y)
                cutter = 0
            direction *= -1

#vertical line
def draw_zigzag_lines_y(points, line_spacing):
    global cutter
    min_x = int(min(point[0] for point in points))
    max_x = int(max(point[0] for point in points))
    min_y = int(min(point[1] for point in points))
    max_y = int(max(point[1] for point in points))

    direction = 1
    for x in range(min_x, max_x, int(line_spacing)):
        line_points = []
        for y in range(min_y, max_y):
            if is_point_in_field(x, y, points):
                line_points.append((x, y))

        if line_points:
            if direction == 1:
                goto(x, line_points[0][1])
                cutter = 1
                goto(x, line_points[-1][1])
                cutter = 0
            else:
                goto(x, line_points[-1][1])
                cutter = 1
                goto(x, line_points[0][1])
                cutter = 0

            direction *= -1
def cutter_on():
    if cutter_equipped == True:
        motor1.run(-600)
        motor2.run(600)
    else:
        pass
def cutter_off():
    if cutter_equipped == True:
        motor1.stop()
        motor2.stop()
    else:
        pass
#Action


"""program"""
press_start()
gyro.reset_angle(0)
draw_zigzag_lines_x(points, line_spacing)
#draw_zigzag_lines_x(points, line_spacing)
