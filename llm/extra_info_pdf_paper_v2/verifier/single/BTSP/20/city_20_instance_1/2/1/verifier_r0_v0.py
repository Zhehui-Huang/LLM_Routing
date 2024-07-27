import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_solution(tour, cities):
    # Requirement 1: The robot must visit each city exactly once, starting and ending at the depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if sorted(tour) != sorted(list(range(len(cities)))):
        return "FAIL"
    
    # Requirement 2: Minimize the longest distance between any two consecutive cities in the tour
    # This cannot be directly verified as "CORRECT" without the optimal value known a priori; we proceed to calculation part.
    max_distance = max(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    
    # Requirement 3: Travel cost is calculated as the Euclidean distance between two cities.
    # Verifying calculated total travel cost and maximum distances
    total_travel_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    if abs(total_travel_cost - 1105.99) > 0.1 or abs(max_distance - 108.23) > 0.1:
        return "FAIL"
    
    return "CORRECT"

# City coordinates as defined in the task
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82),
    (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), (49, 23),
    (78, 76), (68, 45), (50, 28), (69, 9)
]

# Provided solution
tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 11, 13, 14, 15, 16, 17, 19, 18, 0]

# Run verification check
result = check_solution(tour, cities)
print(result)