import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_solution(tour, cost, cities):
    # Check if the tour starts and ends at the depot city
    if not tour or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if the robot visits exactly 7 cities, including the depot city
    if len(set(tour)) != 7:
        return "FAIL"
    
    # Check the calculated total travel cost matches the given Euclidean distance cost
    calculated_cost = 0
    for i in range(1, len(tour)):
        calculated_cost += calculate_euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    
    # This examines if the calculated cost closely matches the provided cost
    if abs(calculated_cost - cost) > 1e-6:
        return "FAIL"

    return "CORRECT"

# Define the cities coordinates
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]

# Solution to verify
tour_solution = []  # This list should contain the indices of cities visited, starting and ending at the depot city (city 0).
total_travel_cost_solution = float('inf')

# Validate the solution
result = validate_solution(tour_solution, total_travel_cost_solution, cities)
print(result)