import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, total_cost, groups, cities):
    # Requirement 1: Start and end at depot 
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly one city from each group
    visited_groups = [False] * len(groups)
    for city_index in tour[1:-1]:  # Excluding the depot city at start and end
        for group_index, group in enumerate(groups):
            if city_index in group:
                if visited_groups[group_index]:
                    return "FAIL"
                visited_sections[group_index] = True
    if not all(visited_groups):
        return "FAIL"
    
    # Requirement 3 and 5: Check total travel cost
    calculated_cost = 0
    for i in range(len(tour)-1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"
    
    # Requirement 4: Output the tour
    # Implicit check in Requirement 1
    return "CORRECT"

# City coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Groups of cities
groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Provided tour and total cost
tour = [0, 1, 5, 7, 9, 8, 2, 3, 0]
total_cost = 279.02

# Check if the solution is correct
result = verify_tour(tour, total_cost, groups, cities)
print(result)