import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, travel_cost, max_distance, cities):
    num_cities = len(cities)
    
    # Check all cities are visited exactly once and the tour starts and ends at depot city 0 [Requirement 1 & 3]
    if tour[0] != 0 or tour[-1] != 0 or sorted(tour) != sorted([0] + list(range(num_cities))):
        return "FAIL"
    
    # Check total calculated travel cost and max distance between consecutive cities [Requirement 5 & 6]
    calculated_total_distance = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_total_distance += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    calculated_total_distance = round(calculated_total, 7)  # Rounding to match precision

    if abs(calculated_total_distance - travel_cost) > 0.0001 or abs(calculated_max_distance - max_distance) > 0.0001:
        return "FAIL"
    
    # If all tests pass
    return "CORRECT"

# Defining cities according to the input problem
cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

# Solution details
tour_solution = [0, 3, 6, 2, 8, 9, 1, 7, 5, 4, 0]
total_travel_cost_solution = 328.58208011724435
maximum_distance_solution = 61.68468205316454

# Verify the solution
result = verify_solution(tour_solution, total_travel_cost_solution, maximum_distance_solution, cities)
print(result)