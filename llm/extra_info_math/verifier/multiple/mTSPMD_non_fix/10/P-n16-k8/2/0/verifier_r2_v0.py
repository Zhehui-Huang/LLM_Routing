import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def check_requirements(tours, costs):
    cities = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
        (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
        (37, 69)
    ]
    
    # Check all robots start at depot city 0
    if not all(tour[0] == 0 for tour in tours):
        return "FAIL"
    
    # Check each robot does not need to return to depot
    # Not explicitly testable through final destinations; assumed by tour format
    
    # Check robots can travel between any two cities
    # Assuming capability; not verifiable by input data
    
    # Check travel cost is calculated correctly
    for tour, claimed_cost in zip(tours, costs):
        total_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
        if not math.isclose(total_cost, claimed_cost, abs_tol=1e-9):
            return "FAIL"
    
    # Check robots need to collectively visit all cities exactly once
    visited = set(city for tour in tours for city in tour)
    if visited != set(range(len(cities))):
        return "FAIL"
    
    # Check each city is visited exactly once and tours are optimized
    # Only unique visits check since optimization cannot be purely verified
    city_count = {}
    for tour in tours:
        for city in tour:
            city_count[city] = city_count.get(city, 0) + 1
    if any(count > 1 for count in city_count.values()):
        return "FAIL"

    return "CORRECT"

# Sample input solution
tours = [
    [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1]
]
costs = [0, 0, 0, 0, 0, 0, 0, 0]

# Unit test execution
result = check_requirements(tours, costs)
print(result)