import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, cities, reported_total_cost, reported_max_distance):
    # Requirement 1: All cities visited exactly once and starts/ends at city 0
    if sorted(tour) != sorted(list(range(len(cities)))) or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 4: Output tour starts and ends at city 0
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    total_distance = 0
    max_distance = 0
    
    for i in range(len(tour) - 1):
        distance = calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_distance += distance
        if distance > max_distance:
            max_distance = distance
    
    # Requirement 5: Check total travel cost
    if not math.isclose(total_distance, reported_total_cost, rel_tol=1e-9):
        return "FAIL"

    # Requirement 6: Check max distance between consecutive cities
    if not math.isclose(max_distance, reported_max_distance, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Define cities coordinates
cities_coordinates = [
    (53, 68), # Depot city 0
    (75, 11), # City 1
    (91, 95), # City 2
    (22, 80), # City 3
    (18, 63), # City 4
    (54, 91), # City 5
    (70, 14), # City 6
    (97, 44), # City 7
    (17, 69), # City 8
    (95, 89)  # City 9
]

# Tour provided as solution
tour_solution = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]

# Reported values
reported_total_cost = 291.41088704894975
reported_max_distance = 56.61271941887264

# Verify the solution based on the requirements
verification_result = verify_solution(tour_solution, cities_coordinates, reported_total_cost, reported_max_distance)
print(verification_result)