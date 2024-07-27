import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, travel_cost, max_distance, cities):
    num_cities = len(cities)

    # Check if the tour starts and ends at the depot city 0 and visits each city exactly once
    if tour[0] != 0 or tour[-1] != 0 or sorted(tour[1:-1]) != sorted(range(1, num_cities)):
        return "FAIL"
    
    # Calculate total travel cost and maximum distance between consecutive cities
    calculated_total_distance = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_total_distance += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance

    # Compare with provided values and allow a small tolerance for floating-point errors
    calculated_total_distance = round(calculated_total_distance, 7)  # Rounding to match precision
    if abs(calculated_total_distance - travel_cost) > 0.0001 or abs(calculated_max_distance - max_distance) > 0.0001:
        return "FAIL"
    
    return "CORRECT"

# Defining cities according to the input problem
cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

# Solution details
tour_solution = [0, 3, 6, 2, 8, 9, 1, 7, 5, 4, 0]
total_travel_cost_solution = 328.58208011724435
maximum_distance_solution = 61.68468205316454

# Verify the solution with corrected variable names
result = verify_solution(tour_solution, total_travel_cost_solution, maximum_distance_solution, cities)
print(result)