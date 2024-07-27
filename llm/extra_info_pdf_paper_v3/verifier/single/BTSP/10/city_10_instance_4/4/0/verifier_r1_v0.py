import math

def calculate_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

def verify_solution(tour, distances, max_dist):
    # Verify requirement 1: Start and end at the depot city, city 0
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # Verify requirement 2: Each city visited exactly once
    if len(set(tour)) != len(tour):
        return "FAIL"
    if set(tour) != set(range(len(distances))):
        return "FAIL"
    
    # Calculate actual maximum distance between consecutive cities
    actual_max_distance = max(
        calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1)
    )
    
    # Verify requirement 3: Minimize the longest distance between any two consecutive cities
    if actual_max_distance > max_dist:
        return "FAIL"
    
    return "CORRECT"

# Coordinates of cities
cities_coordinates = [
    (79, 15),  # City 0
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]

# Extract given solution details
tour = [0, 4, 3, 1, 5, 7, 9, 8, 2, 6, 0]
reported_total_cost = 337.17
reported_max_distance = 61.68

# Convert tour to coordinates for simpler distance calculation
tour_coordinates = [cities_coordinates[i] for i in tour]

# Use verify_solution function to check if the solution meets the requirements
result = verify_solution(tour_coordinates, cities_coordinates, reported_max_distance)
print(result)