import numpy as np

def calculate_distance(x1, y1, x2, y2):
    """ Compute the Euclidean distance between two points (x1, y1) and (x2, y2). """
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_solution(cities_coordinates, tour):
    # Initializations
    total_cost = 0
    max_distance = 0
    num_cities = len(cities_coordinates)

    # Extract x and y coordinates
    x_coords, y_coords = zip(*cities_coordinates)
    
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Tour should start and end at depot city (0)
    
    visited = set()
    for i in range(len(tour) - 1):
        city_from = tour[i]
        city_to = tour[i + 1]
        distance = calculate_distance(x_coords[city_from], y_coords[city_fro...
        total_cost += distance
        max_distance = max(max_distance, distance)
        
        if city_to in visited:
            return "FAIL"  # City visited more than once
        visited.add(city_to)
        
    if len(visited) != num_cities:
        return "FAIL"  # Not all cities were visited
    
    return "CORRECT"

# Cities Coordinates
cities_coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0),
    (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25),
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# Simulated Tour Output
tour = "No valid tour found"

# Unit Test
if tour == "No valid tour found":
    print("FAIL")
else:
    result = verify_solution(cities_coordinates, tour)
    print(result)