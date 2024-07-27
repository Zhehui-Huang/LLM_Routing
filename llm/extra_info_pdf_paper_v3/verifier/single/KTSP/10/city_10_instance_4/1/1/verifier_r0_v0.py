import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_travel_cost, city_coordinates):
    if len(tour) == 0 or total_travel_cost == float('inf'):
        return "FAIL"
    
    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 8 cities are visited (including the depot city)
    if len(tour) != 9:  # Includes returning to the starting city
        return "FAIL"
    
    # Calculate the total travel distance from the tour and compare with the given cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    if abs(calculated_cost - total_travel_cost) > 0.001:  # Allowing a small margin for floating point precision issues
        return "FAIL"
    
    return "CORRECT"

# City coordinates provided in the task
city_coordinates = [
    (79, 15),  # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Test data from the solution provided
tour = []
total_travel_cost = float('inf')

# Run verification
result = verify_solution(tour, total_travel_cost, city_coordinates)
print(result)