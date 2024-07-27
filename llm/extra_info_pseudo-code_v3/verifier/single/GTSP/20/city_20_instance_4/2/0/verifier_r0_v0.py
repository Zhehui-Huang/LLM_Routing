import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_tour(tour, city_positions, city_groups):
    # Check if tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    unique_cities = set(tour) - {0}
    visited_groups = set()
    for city in unique_cities:
        for index, group in enumerate(city_groups):
            if city in group:
                if index in visited_groups:
                    return "FAIL"
                visited_groups.add(index)
                break
    
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Check total travel cost (allowing some margin for floating-point precision)
    expected_cost = 266.71610174713
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_positions[tour[i]], city_positions[tour[i+1]])

    if not math.isclose(calculated_cost, expected_cost, rel_tol=1e-3):
        return "FAIL"

    return "CORRECT"

# City positions indexed by city number
city_positions = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54), 
    18: (64, 72), 19: (14, 89)
}

# Groups of cities
city_groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], 
    [2, 4, 14], [10, 17], [7, 15]
]

# Suggested tour and cost
tour = [0, 5, 18, 13, 1, 14, 10, 15, 0]

# Validate the tour
result = validate_tour(tour, city_positions, city							_groups)
print(result)