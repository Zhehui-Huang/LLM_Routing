import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, total_travel_cost, city_coordinates, city_groups):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Tour must start and end at the depot city 0

    visited_groups = set()
    visited_cities = set()

    compute_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        compute_cost += calculate_distance(city_coordinates[city1], city_coordinates[city2])
        
        if city1 in visited_cities:
            return "FAIL"  # City visited more than once which should not happen
        visited_cities.add(city1)

        for idx, group in enumerate(city_groups):
            if city1 in group:
                visited_groups.add(idx)

    if len(visited_groups) != len(city_groups):
        return "FAIL"  # Not all groups have been visited by the robot exactly once

    if abs(total_travel_cost - compute_cost) > 1e-6:
        return "FAIL"  # Miscalculation in the travel cost

    return "CORRECT"

# Define city coordinates in the same order as mentioned
city_coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Define city groups
city_groups = [
    [1, 2, 5, 6], [8, 9, 10, 13], [3, 4, 7], [11, 12, 14]
]

# Provided tour and cost
provided_tour = [0]  # Incomplete: This should contain a full tour from the provided output
provided_total_travel_cost = 0  # This should match the computed tour cost

# Call verification function
result = verify_tour(provided_tour, provided_total_travel_cost, city_coordinates, city_groups)
print(result)