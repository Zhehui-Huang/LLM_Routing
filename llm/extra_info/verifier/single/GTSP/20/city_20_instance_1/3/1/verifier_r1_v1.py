import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, total_cost_claimed):
    cities = [
        (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), 
        (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
        (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
        (50, 28), (69, 9)
    ]
    groups = [
        [5, 6, 7, 11, 17],
        [1, 4, 8, 13, 16],
        [2, 10, 15, 18, 19],
        [3, 9, 12, 14]
    ]
    
    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 3: Visit exactly one city from each group
    visited_groups = [0] * len(groups)  # Track if each group is visited
    unique_cities = set(tour[1:-1])  # Ignore the starting and ending depot city
    for idx, group in enumerate(groups):
        if len(unique_cities.intersection(group)) != 1:
            return "FAIL"
        visited_groups[idx] = 1  # Mark this group as visited
    
    if not all(visited_groups):
        return "FAIL"
    
    # Requirement 2 & 5: Check the total cost using Euclidean distances
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(total_distance, total_cost_claimed, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Provided solution details
tour = [0, 6, 13, 2, 9, 0]
total_cost_claimed = 114.66

# Check if the provided solution meets all the requirements
result = verify_tour(tour, total_cost_claimed)
print(result)  # This should print "CORRECT" or "FAIL" based on verification