import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(coordinates, tour, total_cost, max_distance):
    # Checking that there are 21 nodes including the depot city
    if len(coordinates) != 20:
        return "FAIL"
    
    # Checking that each node is a tuple with two integer coordinates (x, y)
    if not all(isinstance(city, tuple) and len(city) == 2 for city in coordinates):
        return "FAIL"
    
    # Check that the tour starts and ends at city 0 (depot city)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check each city is visited exactly once
    if len(set(tour)) != len(coordinates) + 1 or len(tour) != 22:
        return "FAIL"

    # Calculate total and maximum consecutive distances
    computed_total_cost = 0
    computed_max_distance = 0
    for i in range(1, len(tour)):
        dist = calculate_distance(coordinates[tour[i-1]], coordinates[tour[i]])
        computed_total_cost += dist
        computed_max_distance = max(computed_max_distance, dist)

    # Compare calculated and provided total cost and max distance
    if not math.isclose(computed_total_cost, total_cost, rel_tol=1e-2) or \
       not math.isclose(computed_max_distance, max_distance, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Coordinates of cities including the depot
coordinates = [
    (30, 56),  # depot city
    (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77),
    (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), 
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Simulated valid output values for a BTSP algorithm
simulated_tour = [0, 4, 7, 14, 8, 12, 18, 3, 1, 10, 11, 16, 9, 15, 17, 5, 2, 13, 6, 19, 0]
simulated_total_cost = 949.43
simulated_max_distance = 114.55

# Perform test verification
test_result = test_solution(coordinates, simulated_tour, simulated_total_cost, simulated_max_distance)
print(test_result)