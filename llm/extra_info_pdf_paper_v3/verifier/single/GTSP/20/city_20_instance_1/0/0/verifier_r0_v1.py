import math

# Coordinates for cities indexed from 0 through 19
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91),
    4: (68, 98), 5: (45, 84), 6: (4, 56), 7: (54, 82),
    8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76),
    12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23),
    16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Groups of city indices
groups = {
    0: [5, 6, 7, 11, 17],
    1: [1, 4, 8, 13, 16],
    2: [2, 10, 15, 18, 19],
    3: [3, 9, 12, 14]
}

# Proposed tour and its cost
proposed_tour = [0, 6, 13, 2, 9, 0]
proposed_cost = 114.66

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution(tour, cost):
    # Check if the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if the tour covers one city from each group
    visited_groups = []
    for city in tour[1:-1]:  # excluding the depot at the start and end
        for group_index, group_cities in groups.items():
            if city in group_cities:
                visited_groups.append(group_index)
    if sorted(visited_groups) != sorted(groups.keys()):
        return "FAIL"
    
    # Calculate the total travel cost of the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Check if the provided cost matches the calculated cost within precision
    if not math.isclose(calculated_cost, cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Execute the test
result = test_solution(proposed_tour, proposed_cost)
print(result)