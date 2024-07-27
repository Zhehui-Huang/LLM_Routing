import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, total_travel_cost, max_distance_between_cities):
    cities = [
        (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82), 
        (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), 
        (72, 43), (6, 99)
    ]
    
    # Check if all cities are visited exactly once
    if len(tour) != len(cities) + 1:
        return "FAIL"
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if len(set(tour)) != len(cities) + 1:
        return "FAIL"

    # Check total travel cost and maximum distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    
    for i in range(len(tour) - 1):
        distance = calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    # Check the precision of floating point calculations
    if not (abs(calculated_total_cost - total_travel_cost) < 1e-6 and 
            abs(calculated_max_distance - max_distance_between_cities) < 1e-6):
        return "FAIL"

    return "CORRECT"

# Provided solution to verify
tour = [0, 6, 11, 8, 1, 14, 12, 4, 3, 10, 5, 9, 13, 7, 2, 0]
total_travel_cost = 322.5037276986899
max_distance_between_cities = 64.66065264130884

# Run the test
result = test_solution(tour, total_travel_cost, max_distance_between_cities)
print(result)