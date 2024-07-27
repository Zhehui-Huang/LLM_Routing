import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_tour(city_positions, tour, expected_cost):
    # Requirement 1: Start and end at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly one city from each city group
    groups = [[2, 7, 10, 11, 14], [1, 3, 5, 8, 13], [4, 6, 9, 12]]
    visited_groups = []
    for city_index in tour[1:-1]:  # Exclude the depot city
        for i, group in enumerate(groups):
            if city_index in group:
                visited_groups.append(i)
    if sorted(list(set(visited_groups))) != [0, 1, 2]:
        return "FAIL"
    
    # Requirement 3 & 5: Calculate and check total travel cost using Euclidean distance
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(city_positions[tour[i]], city_positions[tour[i+1]])
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-2):
        return "FAIL"
    
    # All checks passed
    return "CORRECT"

# City positions representing depot 0 and cities 1-14
city_positions = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77), (63, 23), (19, 76), 
                  (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

# Given tour and its respected total travel cost
tour = [0, 10, 1, 9, 0]
total_travel_cost = 122.22

# Check the solution
result = check_tour(city_positions, tour, total_travel_cost)
print(result)