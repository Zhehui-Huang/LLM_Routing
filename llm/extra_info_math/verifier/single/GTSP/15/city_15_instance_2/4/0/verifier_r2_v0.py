import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(solution_tour, solution_cost, cities, groups):
    # Requirement 1: Start and end at depot city 0
    if solution_tour[0] != 0 or solution_tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly one from each group
    visited_groups = [0 for _ in groups]  # Tracker for group visits
    visited_cities = set()
    
    for city in solution_tour:
        if city in visited_cities and city != 0:  # Exclude depot revisits
            return "FAIL"
        visited_cities.add(city)
        for group_index, group in enumerate(groups):
            if city in group:
                visited_groups[group_index] += 1
    
    if any(visits != 1 for visits in visited_groups):
        return "FAIL"
    
    # Requirement 3: Minimize total travel cost
    calculated_cost = 0
    for i in range(len(solution_tour) - 1):
        city_i = solution_tour[i]
        city_j = solution_tour[i + 1]
        calculated_cost += euclidean_distance(cities[city_i][0], cities[city_i][1], cities[city_j][0], cities[city_j][1])
    
    if abs(calculated_cost - solution_cost) > 1e-5:  # Allow for floating point precision issues
        return "FAIL"
    
    return "CORRECT"

# City coordinates
cities_coordinates = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 5: (36, 30), 6: (52, 82), 
    7: (93, 44), 8: (21, 78), 9: (68, 14), 10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# City groups
city_groups = [
    [8, 12, 14], [7, 10, 11], [4, 6, 9], [1, 3, 13], [2, 5]
]

# Solution tour and cost as given
tour = [0, 6, 0]
cost = 10.770329614269007

# Call the verification function
result = verify_tour(tour, cost, cities_coordinates, city_groups)
print(result)