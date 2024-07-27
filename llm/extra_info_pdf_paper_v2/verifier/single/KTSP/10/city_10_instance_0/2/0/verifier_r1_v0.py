import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost, cities):
    if len(tour) != 5 or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    if len(set(tour)) != 4:
        return "FAIL"
    
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Allow a small margin for floating point arithmetic imprecision.
    if abs(calculated_cost - total_cost) > 0.01:
        return "FAIL"
    
    return "CORRECT"

# City coordinates.
cities = [
    (50, 42), # City 0
    (41, 1),  # City 1
    (18, 46), # City 2
    (40, 98), # City 3
    (51, 69), # City 4
    (47, 39), # City 5
    (62, 26), # City 6
    (79, 31), # City 7
    (61, 90), # City 8
    (42, 49)  # City 9
]

# Solution provided.
tour = [0, 9, 5, 6, 0]
total_cost = 61.66

# Run verification.
result = verify_solution(tour, total_cost, cities)
print(result)