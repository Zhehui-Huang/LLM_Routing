import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, cost, coords):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    # Check if the robot visits exactly 7 unique cities including the depot city
    if len(set(tour)) != 7:
        return "FAIL"
    # Check if the only cities in tour are from the available cities
    if not all(city in range(len(coords)) for city in tour):
        return "FAIL"
    # Calculate the tour cost and compare with the provided cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(coords[tour[i]], coords[tour[i + 1]])
    if not math.isclose(calculated_cost, cost, rel_tol=1e-2):  # Allow some tolerance
        return "FAIL"
    # If all checks passed
    return "CORRECT"

# City coordinates
cities_coordinates = [
    (84, 67),  # city 0 (depot)
    (74, 40),  # city 1 
    (71, 13),  # city 2 
    (74, 82),  # city 3 
    (97, 28),  # city 4 
    (0, 31),   # city 5 
    (8, 62),   # city 6 
    (74, 56),  # city 7 
    (85, 71),  # city 8 
    (6, 76)    # city 9 
]

# Provided tour and cost
tour = [0, 8, 3, 7, 1, 2, 4, 0]
cost = 159.97

# Check the solution
result = verify_solution(tour, cost, cities_coordinates)
print(result)