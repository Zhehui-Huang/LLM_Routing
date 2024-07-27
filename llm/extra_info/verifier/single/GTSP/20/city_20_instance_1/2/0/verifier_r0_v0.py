import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost):
    # Coordinates of each city indexed by city number
    cities = {
        0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
        5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 
        10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
        15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
    }
    
    # Group definitions
    groups = {
        0: [5, 6, 7, 11, 17],
        1: [1, 4, 8, 13, 16],
        2: [2, 10, 15, 18, 19],
        3: [3, 9, 12, 14]
    }
    
    # Check Requirement 1: Start and end at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2: Visit exactly one city from each group
    visited_groups = set()
    for city in tour[1:-1]:  # Exclude the initial and final depot visit
        for group_id, group_cities in groups.items():
            if city in group_cities:
                visited_groups.add(group_id)
    
    if len(visited_groups) != 4:
        return "FAIL"

    # Check Requirement 3: Total travel cost is calculated using the Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, abs_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Given solution details
tour = [0, 6, 13, 2, 9, 0]
total_cost = 114.65928837582914

# Check if the solution is correct
result = verify_solution(tour, total_cost)
print(result)