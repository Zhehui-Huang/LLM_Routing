import math

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities given their coordinates."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_travel_cost, groups, cities):
    """
    Verify the given tour solution based on the specified requirements.
    
    Args:
    - tour: list of city indices representing the robot's tour.
    - total_travel_cost: provided total travel cost.
    - groups: list of lists with each sublist representing a group of city indices.
    - cities: list of tuples where each tuple represents the coordinates of a city.
    
    Returns:
    - "CORRECT" if all requirements are met and the calculated travel cost matches the given cost,
      otherwise "FAIL".
    """
    # [Requirement 1]: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2]: Visit exactly one city from each of the 6 defined groups
    visited_from_groups = [False] * len(groups)
    for index, city in enumerate(tour[1:-1]):  # skipping the first and the last city (depot)
        for g_index, group in enumerate(groups):
            if city in group:
                if visited_from_groups[g_index]:
                    return "FAIL"
                visited_from_groups[g_index] = True
                break
    
    if not all(visited_from_groups):
        return "FAIL"
    
    # [Requirement 3]: Calculate the correct total cost based on Euclidean distance
    calculated_cost = 0
    for i in range(len(tour)-1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_travel_cost, abs_tol=1e-1):
        return "FAIL"
    
    return "CORRECT"

# Data setup
cities = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77), (98, 95), 
          (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)]
groups = [[4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]]
tour = [0, 4, 7, 12, 15, 3, 18, 0]
total_travel_cost = 227.4

# Verification
result = verify_solution(tour, total_travel_cost, groups, cities)
print(result)