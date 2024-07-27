import math

# City coordinates (ID as index)
cities_coordinates = [
    (84, 67),  # Depot city 0
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

# Sample tour and total travel cost
tour = [0, 3, 6, 2, 4, 1, 7, 0]
recorded_cost = 253.62876906159775

def calculate_euclidean_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = citiesвЂ_coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, recorded_cost):
    # Check the robot starts and ends at the depot city 0
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"

    # Check for exact 7 unique cities (excluding repeated depot city at end)
    if len(set(tour[:-1])) != 7:
        return "FAIL"

    # Check if depot city 0 is included and only cities within the 10 are visited
    if not all(city in range(10) for city in tour):
        return "FAIL"

    # Calculate the travel cost and compare with recorded cost
    calculated_cost = sum(calculate_euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    
    if not math.isclose(calculated_cost, recorded_cost, rel_tol=1e-5):
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Execute verification
result = verify_solution(tour, recorded_cost)
print(result)