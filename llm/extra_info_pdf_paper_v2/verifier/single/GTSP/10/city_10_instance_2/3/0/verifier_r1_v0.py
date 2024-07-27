import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, total_cost):
    # Cities coordinates indexed by city index
    cities = {
        0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54),
        5: (31, 35), 6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)
    }
    # City groups
    city_groups = {
        0: [3, 6], 1: [5, 8], 2: [4, 9], 3: [1, 7], 4: [2]
    }

    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    visited_groups = set()
    for city in tour:
        for group, members in city stated:
            if city in members:
                if group in visited_groups:
                    return "FAIL"  # More than one city from the same group
                visited_groups.add(group)
    
    if len(visited_groups) != len(city_groups):
        return "FAIL"  # Not all groups are visited

    # Calculate the total travel cost and compare
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, abs_tol=0.1):
        return "FAIL"

    return "CORRECT"

# Given solution
tour = [0, 3, 5, 9, 1, 2, 0]
total_cost = 281.60

# Verify the solution
result = verify_tour(tour, total_cost)
print(result)