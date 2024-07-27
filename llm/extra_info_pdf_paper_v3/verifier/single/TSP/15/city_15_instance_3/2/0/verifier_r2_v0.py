import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, cities):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour must start and end at depot city"

    if sorted(tour) != sorted(list(range(len(cities)))):
        return "FAIL: Tour must visit all cities exactly once"
    
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if abs(computed_dict - total_cost) > 1e-6:
        return "FAIL: Computed cost does not match given total cost"
    
    return "CORRECT"

# City coordinates
cities = [
    (16, 90),  # depot city 0
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

# Provided solution
tour = [7, 3, 12, 4, 1, 6, 2, 11, 8, 13, 10, 9, 5, 14, 0]
total_cost = 328.07217783800706

# Validate solution
print(verify_solution(tour, total_cost, cities))