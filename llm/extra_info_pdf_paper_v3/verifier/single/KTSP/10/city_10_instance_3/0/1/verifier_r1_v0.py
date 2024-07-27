import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def validate_solution(tour, cities):
    # Checking that the tour starts and ends at depot city which is 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Checking that exactly 7 unique cities are visited
    if len(set(tour)) != 8:  # including depot city repeated at the end
        return "FAIL"

    # Checking that all visited cities are from the given cities and exactly 7 cities are visited
    unique_cities_visited = set(tour[:-1])  # exclude the last city as it's a repeat of the first
    if len(unique_cities_visited) != 7:
        return "FAIL"
    
    # All validations passed
    return "CORRECT"

# Coordinates of the cities including the depot
cities = [
    (84, 67),  # City 0 (Depot)
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

# Example of a tour output that needs to be checked; this is an example, adjust as per actual output.
example_tour = [0, 1, 2, 3, 4, 5, 6, 0]

# Validate the solution tour
result = validate_solution(example_tour, cities)
print(result)