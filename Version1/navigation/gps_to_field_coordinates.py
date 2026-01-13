import turtle
import math

# Earth's radius in meters
R = 6371000

def gps_to_xy(reference_lat, reference_lon, lat, lon):
    # Convert degrees to radians
    reference_lat_rad = math.radians(reference_lat)
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)
    reference_lon_rad = math.radians(reference_lon)
    
    # Calculate deltas
    delta_lon = lon_rad - reference_lon_rad
    delta_lat = lat_rad - reference_lat_rad
    
    # Convert to Cartesian coordinates
    x = delta_lon * math.cos(reference_lat_rad) * R
    y = delta_lat * R
    return x, y

# rotate coordinates around the origin (0,0)
def rotate_coordinates(coordinates, angle_rad):
    rotated_coordinates = []
    for x, y in coordinates:
        # Apply rotation transformation
        x_new = x * math.cos(angle_rad) - y * math.sin(angle_rad)
        y_new = x * math.sin(angle_rad) + y * math.cos(angle_rad)
        rotated_coordinates.append((x_new, y_new))
    return rotated_coordinates

# get user input for GPS coordinates in decimal format
def get_gps_coordinates():
    coordinates = []
    print("Enter GPS coordinates in decimal format (e.g., 14.09705, 99.45778). Type 'done' when finished:")
    while True:
        user_input = input("Enter latitude and longitude separated by a comma: ")
        if user_input.lower() == 'done':
            break
        try:
            lat, lon = map(float, user_input.split(','))
            coordinates.append((lat, lon))
        except ValueError:
            print("Invalid input. Please enter the coordinates in 'latitude,longitude' format.")
    return coordinates

#GPS coordinates from user
gps_coordinates = get_gps_coordinates()

#scaling factor from user
scaling_factor = float(input("Enter the scaling factor (Turtle unit per meter): "))

# Reference point (first GPS coordinate)
reference_lat, reference_lon = gps_coordinates[0]

# GPS coordinates to Cartesian coordinates
cartesian_coordinates = [gps_to_xy(reference_lat, reference_lon, lat, lon) for lat, lon in gps_coordinates]

# Scale the Cartesian coordinates
scaled_coordinates = [(x * scaling_factor, y * scaling_factor) for x, y in cartesian_coordinates]


screen = turtle.Screen()
screen.title("GPS to Cartesian Coordinates with Rotation")
t = turtle.Turtle()

# starting point (0, 0)
t.penup()
t.goto(0, 0)
t.pendown()

# Function to rotate based on user input
def rotate_based_on_input(input_type):
    if input_type == 'y':
        # Rotate so that the second point aligns with the y-axis
        second_point_x, second_point_y = scaled_coordinates[1]
        rotation_angle_rad = math.atan2(second_point_x, second_point_y)
    elif input_type == 'x':
        # Rotate so that the last point aligns with the x-axis
        last_point_x, last_point_y = scaled_coordinates[-1]
        if last_point_x == 0:
            rotation_angle_rad = math.pi / 2 if last_point_y > 0 else -math.pi / 2
        else:
            rotation_angle_rad = math.atan2(-last_point_y, last_point_x)
    else:
        print("Invalid input type. Please enter 'x' or 'y'.")
        return
    
    # Rotate coordinates around the origin
    rotated_coordinates = rotate_coordinates(scaled_coordinates, rotation_angle_rad)
    
    # Draw the shape
    points = []
    for x, y in rotated_coordinates:
        t.goto(x, y)
        points.append((x, y))
    print("points =", points)
    t.goto(0, 0)

# input for rotation type ('x' or 'y')
rotation_type = input("Enter rotation type ('x' for last point = (x,0), 'y' for second point = (0,y)): ")

# Call the rotate function based on user input
rotate_based_on_input(rotation_type)

turtle.done()

"""
14.0971129, 99.4578221
14.0979670, 99.4582835
14.0973973, 99.4594370
14.0967392, 99.4589777
done
2
y

14.1799425, 99.4541422
14.1793011, 99.4513856
14.1799228, 99.4510390
14.1817887, 99.4519083
14.1820687, 99.4530611
done
1
y


"""
