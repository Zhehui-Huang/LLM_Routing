import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def validate_solution(tour, cities):
    # Check that the tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check that each city is visited exactly once
    unique_cities = set(tour[1:-1])  # exclude the starting and ending depot city
    if len(unique_cities) != len(cities) - 1:
        return "FAIL"
    
    # Verify if the max distance in the tour is minimized
    # Since no optimal value provided this check would be simple max distance verification
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        if dist > max_distance:
            max_distance = dist
    
    expected_max_distance = 89.58794561770016
    if not math.isclose(max_distance, expected_max_distance, abs_tol=0.0001):
        return "FAIL"

    return "CORRECT"

# City coordinates
cities_coord = [
    (79, 15),  # City 0
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]

# Provided solution tour
provided_tour = [0, 2, 8, 6, 7, 9, 5, 3, 4, 1, 0]

# Validate the solution
result = validate_solution(provided_tour, cities_coord)
print(result)