import math

# Define city coordinates, using index to represent city ID
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

# Provided Tour and Total Travel Cost
tour = [0, 3, 6, 2, 4, 1, 7, 0]
recorded_cost = 253.62876906159775

def calculate_euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, recorded_cost):
    """Verify if the provided solution meets all the specified requirements."""
    # Check if there are 7 unique cities visited, excluding the final depot return
    unique_cities = set(tour[:-1])
    if len(unique_cities) != 7 or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all cities in the tour are valid (based on the total number of cities)
    if any(city < 0 or city >= len(cities_coordinates) for city in tour):
        return "FAIL"

    # Calculate total travel cost from the tour
    calculated_cost = sum(calculate_euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    
    # Compare the calculated cost with the provided cost
    if not math.isclose(calculated_cost, recorded_cost, rel_tol=1e-3):
        return "FAIL"

    return "CORRECT"

# Calling the verification function and printing the result
result = verify_solution(tour, recorded_cost)
print(result)