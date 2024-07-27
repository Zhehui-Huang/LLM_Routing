import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, total_travel_cost, cities_coordinates, city_groups):
    if not tour or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Check start and end at depot
    
    # Check if only one city from each group is visited
    unique_cities = set(tour)
    group_visit_count = {g: 0 for g in range(len(city_groups))}
    for city in unique_cities:
        for idx, group in enumerate(city_groups):
            if city in group:
                group_visit_count[idx] += 1

    if any(count != 1 for count in group_visit_count.values()):
        return "FAIL"

    # Calculate the actual tour cost and match with given
    calculated_cost = sum(calculate_euclidean_distance(cities_coordinates[tour[i]][0], 
                                                       cities_coordinates[tour[i]][1],
                                                       cities_coordinates[tour[i + 1]][0],
                                                       cities_coordinates[tour[i + 1]][1])
                          for i in range(len(tour) - 1))

    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-6):
        return "FAIL"

    return "CORRECT"

# Given example
cities_coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

city_groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

tour = [0, 12, 10, 4, 3, 2, 0]
total_travel_cost = 138.15244358342136

# Verify the solution
result = verify_solution(tour, total_travel_cost, cities_coordinates, city_groups)
print(result)