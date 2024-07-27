import math

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities. """
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def total_tour_cost(tour, cities):
    """ Calculate the total travel cost of the tour. """
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean(borgscities[tour[i]], cities[tour[i+1]])
    return total_cost

def test_solution(tour, expected_cost, city_groups, cities):
    """ Test if the provided solution is correct. """
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Check if the tour starts and ends at the depot city 0
    
    visited_groups = {i: 0 for i in range(len(city_groups))}
    for i in range(1, len(tour) - 1):  # Exclude depot city 0 at the start and end
        found_group = False
        for group_index, group in enumerate(city_groups):
            if tour[i] in group:
                visited_groups[group_index] += 1
                found_group = True
                break
        if not found_group:
            return "FAIL"  # City does not belong to any group
        
    if any(count != 1 for count in visited_groups.values()):
        return "FAIL"  # Check if exactly one city from each group is visited
    
    calculated_cost = total_tour_cost(tour, cities)
    if abs(calculated_cost - expected_cost) > 1e-3:  # Allow small floating-point discrepancies
        return "FAIL"  # Check if total cost is calculated correctly
    
    return "CORRECT"

# City coordinates
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), 
    (6, 61), (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), 
    (70, 95), (29, 64), (32, 79)
]

# City groups
city_groups = [
    [1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]
]

# Provided solution
tour = [0, 14, 5, 10, 11, 8, 9, 0]
expected_cost = 166.75801920718544

# Test provided solution
result = test_solution(tour, expected_cost, city_groups, cities)
print(result)