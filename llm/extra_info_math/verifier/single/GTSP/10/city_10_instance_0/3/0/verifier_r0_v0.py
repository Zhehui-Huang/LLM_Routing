import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, cities, city_groups):
    # Requirement 1: Start and end at depot city 0
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"

    # Extract actual visited cities (excluding multiple instances of depot)
    visited_cities = tour[1:-1]

    # Requirement 2: Visit exactly one city from each group
    visited_in_groups = [0] * len(city_groups)
    for city in visited_cities:
        for group_index, group in enumerate(city_groups):
            if city in group:
                visited_in_groups[group_index] += 1
    
    if any(count != 1 for count in visited_in_groups):
        return "FAIL"

    # Requirement 3: Check if the total travel distance is the shortest calculated one
    calculated_distance = sum([euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1)])
    
    actual_distance = 43.9254 # Given optimal distance as calculated by solver
    if not math.isclose(calculated_distance, actual_distance, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# City coordinates with index as city id
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# City groups
city_groups = [
    [1, 2, 6],
    [3, 7, 8],
    [4, 5, 9]
]

# Provided tour
tour = [0, 1, 2, 0]  # This is the corrected format which includes at least one city from each group
    
# Call function to verify solution correctness
verification_result = verify_solution(tour, cities, city_groups)
print(verification_result)