import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution():
    # City coordinates index by city number
    cities = {
        0: (84, 67),
        1: (74, 40),
        2: (71, 13),
        3: (74, 82),
        4: (97, 28),
        5: (0, 31),
        6: (8, 62),
        7: (74, 56),
        8: (85, 71),
        9: (6, 76)
    }
    
    # City groups as sets to simplify checking for membership
    city_groups = [
        {7, 9},
        {1, 3},
        {4, 6},
        {8},
        {5},
        {2}
    ]
    
    proposed_solution = [0, 7, 1, 4, 8, 5, 2, 0]
    proposed_cost = 324.1817486177585
    
    # Check if the tour starts and ends at the depot
    if proposed_solution[0] != 0 or proposed_solution[-1] != 0:
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    visited_groups = []
    for city in proposed_solution[1:-1]:  # Skip the depot at start and end
        for index, group in enumerate(city_groups):
            if city in group:
                if index in visited_groups:
                    return "FAIL"
                visited_groups.append(index)
    
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Calculate the actual travel cost
    actual_cost = 0
    for i in range(len(proposed_solution) - 1):
        actual_cost += euclidean_distance(cities[proposed_solution[i]], cities[proposed_solution[i+1]])
    
    # Check if the calculated cost matches the proposed cost (allowing for floating point differences)
    if not math.isclose(actual_cost, proposed_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Verify the proposed solution
print(check_solution())