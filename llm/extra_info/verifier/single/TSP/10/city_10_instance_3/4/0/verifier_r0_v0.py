import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(route, cost, city_coordinates):
    # Check if tour starts and ends at depot city, city 0
    if route[0] != 0 or route[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited once and exactly once
    visited = set(route)
    if visited != set(range(len(city_coordinates))):
        return "FAIL"
    
    # Check if total travel cost is calculated correctly
    calculated_cost = 0
    for i in range(len(route) - 1):
        calculated_cost += euclidean_distance(city_coordinates[route[i]], city_coordinates[route[i + 1]])
    
    # Round the calculated cost for float comparison accuracy
    if round(calculated_cost, 1) != cost:
        return "FAIL"
    
    return "CORRECT"

# City coordinates including the depot
city_coordinates = [
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

# Provided solution
tour = [0, 8, 3, 9, 6, 5, 7, 1, 2, 4, 0]
total_travel_cost = 326.5

# Verify the solution
result = verify_solution(tour, total_travel_calculated, city_coordinates)
print(result)  # Output should be "CORRECT" or "FAIL"