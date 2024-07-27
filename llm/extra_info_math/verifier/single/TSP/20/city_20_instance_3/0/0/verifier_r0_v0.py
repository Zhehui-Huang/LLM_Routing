def calculate_euclidean_distance(city1, city2):
    from math import sqrt
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_travel_cost, cities):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour must start and end at the depot city 0."

    if len(set(tour)) < len(cities):
        return "FAIL: Not all cities are visited."

    if sorted(set(tour)) != sorted(list(range(len(cities)))):
        return "FAIL: Not every city is visited exactly once."

    calculated_cost = 0
    for i in range(1, len(tour)):
        calculated_cost += calculate_euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    
    if not abs(calculated_traffic_cost - total_traffic_cost) < 0.0001:
        return "FAIL: Total travel cost is not correctly calculated."

    return "CORRECT"

# Define cities as per the problem
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), 
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0), 
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), 
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Given values from solution
tour = [0, 3, 0]
total_travel_cost = 336.5650898100357

# Verify the solution
verification_result = verify_solution(tour, total_travel_cost, cities)
print(verification_result)