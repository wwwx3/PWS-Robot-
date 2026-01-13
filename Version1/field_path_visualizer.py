from math import atan2, sqrt, degrees
import turtle

t = turtle.Turtle()

t.speed(10)
t.pensize(3)
t.pendown()

current_x = 0
current_y = 0
current_angle = 0
unit = 2 #square per unit

"input points[]"

#ggearth1 
points = [(0.0, 0.0), (0.0, 214.4358555270136), (279.1832048270756, 217.6809844882485), (259.35487773870204, 42.0651264766684)]
#ggearth2 points = [(0.0, -0.0), (0.0, 305.6189289130089), (75.94102276679222, 325.8207048937061), (255.82097614570586, 186.27367112376214), (257.093483089354, 58.15956789673297)]   
#square  points = [(0,0),(0,120),(120,120),(120,0)]
#pentagon points = [(0,0),(70,0),(120,60),(120,120),(70,180),(0,180)]
#Trapezoid points = [(0,0),(0,160),(120,90),(120,0)]
#Octagon points = [(40,0),(70,0),(120,50),(120,110),(60,180),(30,180),(0,150),(0,30)]
#demo
points = [(0,0),(60,0),(90,20),(60,60),(90,120),(0,120),(20,60)]

line_spacing = 20

def is_point_in_polygon(x, y, points):
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


def draw_polygon(points):
    goto(points[0][0], points[0][1])
    print(points[0][0], points[0][1])
    for point in points:
        goto(point[0], point[1])
        print(point[0], point[1])
    goto(points[0][0], points[0][1])
    print(points[0][0], points[0][1])
    # Close the polygon

    return t

#horizontal line
def draw_zigzag_lines_x(points, line_spacing):
    min_x = int(min(point[0] for point in points))
    max_x = int(max(point[0] for point in points))
    min_y = int(min(point[1] for point in points))
    max_y = int(max(point[1] for point in points))
    
    direction = 1
    t.color("blue")
    for y in range(min_y, max_y, line_spacing):
        line_points = []
        for x in range(min_x, max_x):
            if is_point_in_polygon(x, y , points):
                line_points.append((x, y))
                print((x,y))

        if line_points:
            if direction == 1:
                goto(line_points[0][0], y)
                goto(line_points[-1][0], y)
            else:
                goto(line_points[-1][0], y)
                goto(line_points[0][0], y)
            direction *= -1

#vertical line
def draw_zigzag_lines_y(points, line_spacing):
    min_x = int(min(point[0] for point in points))
    max_x = int(max(point[0] for point in points))
    min_y = int(min(point[1] for point in points))
    max_y = int(max(point[1] for point in points))
    t.color("blue")
    direction = 1
    for x in range(min_x, max_x, line_spacing):
        line_points = []
        for y in range(min_y, max_y):
            if is_point_in_polygon(x, y, points):
                line_points.append((x, y))

        if line_points:
            if direction == 1:
                goto(x, line_points[0][1])
                goto(x, line_points[-1][1])
            else:
                goto(x, line_points[-1][1])
                goto(x, line_points[0][1])

            direction *= -1






def move(distance = 0, speed = 0):
    """Move the robot forward or backward by a specific distance in centimeters."""
    while robot.distance() < distance:
        robot.drive(speed,0)
    brake()
    robot.reset()

def turn(angle = 0, speed = 0):
    """Turn the robot by a specific angle in degrees."""
    # Reset the gyro sensor
    gyro.reset_angle(0)
    # Determine the direction of the turn
    
    if gyro.angle() < angle:
        while gyro.angle() < angle:
            robot.drive(0, speed)
    else:
        while gyro.angle() > angle:
            robot.drive(0, -speed)
    brake()

def goto(target_x,target_y):
    
    global current_x, current_y, current_angle
   
    dx = target_x - current_x
    dy = target_y - current_y
    distance = sqrt(dx**2 + dy**2)
    distance = distance*unit
    target_angle = degrees(atan2(dy, dx))

    turn_angle = target_angle - current_angle
    if turn_angle > 180:
        turn_angle = -1*(360 - turn_angle)
    if turn_angle < -180:
        turn_angle = -1*(-360 - turn_angle)
    
    
    
    t.left(turn_angle)
    t.forward(distance)

    current_x = target_x
    current_y = target_y
    current_angle = target_angle


# Write your program here.


 


draw_polygon(points)
t.speed(3)
draw_zigzag_lines_x(points, line_spacing)

turtle.done()

# Get user choice
"""
num_points = int(input("Enter the number of points for your polygon: "))

for i in range(num_points):
    x = int(input(f"Enter x coordinate for point {i + 1}: "))
    y = int(input(f"Enter y coordinate for point {i + 1}: "))
    points.append((x, y))

pattern_choice = input("Enter the line pattern direction (x for X-axis, y for Y-axis): ").lower()

if pattern_choice == 'x':
    draw_zigzag_lines_x(points, line_spacing)
elif pattern_choice == 'y':
    draw_zigzag_lines_y(points, line_spacing)
else:
    print("Invalid choice. Please enter 'x' or 'y'.")


while robot.distance() < (y2 - y1)* unit:
    robot.drive(250,0)
robot.stop()
brake()

4
0
0
0
100
100
100
100
0
20
x
y


"""

    
    
"""
# Initialize the motors
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Define the wheel diameter (in mm) and axle track (distance between the centers of the wheels, in mm)
wheel_diameter = 56
axle_track = 107

# Create a DriveBase instance
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

robot.drive(200,0)
"""
