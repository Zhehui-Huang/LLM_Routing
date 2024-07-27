import math

def compute_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def validate_tour(city_coordinates, tour):
    n = len(city_coordinates)
    
    # Check if all cities are visited exactly once and tour starts and ends at depot city 0
    if set(tour) != set(range(n)) or tour[0] != 0 or tour[-1] != 0:
        return "FAIL", "Tour does not include all cities exactly once or does not start/end at depot."
    
    # Check if each segment distance is within allowable range
    max_distance = 0
    total_distance = 0
    for i in range(len(tour)-1):
        distance = compute_euclidean_distance(city_coordinates[tour[i]][0], city_coordinates[tour[i]][1], 
                                              city_coordinates[tour[i+1]][0], city_coordinates[tour[i+1]][1])
        total_distance += distance
        if distance > max_distance:
            max_distance = distance

    expected_total_distance = 643.1678994084214
    expected_max_distance = 86.33075929238663
    if abs(total_distance - expected_total_trip_cost) > 1e-5 or abs(max_distance - expected_max_distance) > 1e-5:
        return "FAIL", "Invalid total distance or maximum distance between cities."

    return "CORRECT", None

# Cities coordinates including depot
cities_coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), 
    (54, 93), (34, 73), (6, 61), (86, 69), 
    (30, 50), (35, 73), (42, 64), (64, 30), 
    (70, 95), (29, 64), (32, 79)
]

# Provided solution
tour = [0, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Check the solution
result, message = validate_tour(cities_coordinates, tour)

# Output the result
if result == "CORRECT":
    print("CORRECT")
else:
    print("FAIL")
    print(message)