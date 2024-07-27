import numpy as np

def calculate_distance(x1, y1, x2, y2):
    """Compute the Euclidean distance between two points (x1, y1) and (x2, y2)."""
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_solution(cities_coordinates, tour):
    """Verify the tour meets all given requirements."""
    if tour == "No valid tour found":
        return "FAIL: No tour provided"

    total_cost = 0
    max_distance = 0
    num_cities = len(cities_coordinates)
    
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start and end at the depot city"  # Start/End at depot

    visited = set()
    for i in range(len(tour) - 1):
        city_from = tour[i]
        city_to = tour[i + 1]
        distance = calculate_distance(cities_coordinates[city_from][0], cities_coordinates[city_from][1],
                                      cities_coordinates[city_to][0], cities_coordinates[city_to][1])
        total_cost += distance
        max_distance = max(max_distance, distance)
        
        if city_to in visited and city_to != 0:  # Include condition for returning to start
            return "FAIL: City visited more than once"  # Repeat visit other than start
        visited.add(city_to)
        
    if len(visited) < num_cities:
        return "FAIL: Not all cities were visited"  # All cities visited
    
    return "CORRECT"

# Cities Coordinates
cities_coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25),
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# Simulated Tour Output - should be a list, not a string
tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]

# Run Unit Test
result = verify_solution(cities_coordinates, tour)
print(result)