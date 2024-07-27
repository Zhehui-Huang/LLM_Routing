import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def validate_tour(tour, city_groups, city_positions):
    # Check if tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if every city from each group is visited exactly once and no other
    group_visited = set()
    cities_visited = set(tour)
    for index, city in enumerate(tour):
        for group_index, group in enumerate(city_groups):
            if city in group:
                if group_index in group_visited:
                    return "FAIL"
                else:
                    group_visited.add(group_index)
                    
    if len(group_visited) != len(city_groups):
        return "FAIL"

    # Check if cities in tour match the city indices provided and calculate total travel cost
    total_calculated_cost = 0
    for i in range(1, len(tour)):
        if tour[i] not in range(len(city_positions)):
            return "FAIL"
        total_calculated_cost += calculate_euclidean_distance(
            city_positions[tour[i-1]], city_positions[tour[i]]
        )
    
    # Allow slight variation due to floating-point arithmetic
    if not math.isclose(total_calculated_cost, 266.71610174713, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# City coordinates
city_positions = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Groups of cities
city_groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13],
    [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]
]

# Provided tour
tour_solution = [0, 5, 18, 13, 1, 14, 10, 15, 0]

# Validate the tour
result = validate_tour(tour_solution, city_groups, city_positions)
print(result)