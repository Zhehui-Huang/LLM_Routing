import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_solution(tour, cost, cities):
    # Check if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if the robot visits exactly 7 cities, including the depot city
    if len(set(tour)) != 7:
        return "FAIL"
    
    # Check if the total travel cost matches Euclidean distance
    calculated_cost = 0
    for i in range(1, len(tour)):
        calculated_cost += calculate_euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    
    if abs(calculated_cost - cost) > 1e-6:
        return "FAIL"

    return "CORRECT"

# Define the cities coordinates
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]

# Solution to verify
tour_solution = []
total_travel_cost_solution = float('inf')

# Validate the solution
result = validate_solution(tour_solution, total_travel_data_notificationost_solution, cities)
print(result)