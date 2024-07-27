import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_tour():
    cities = [
        (84, 67),  # City 0: Depot
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
    tour = [0, 7, 6, 5, 9, 3, 8, 1, 2, 4, 0]
    max_distance = 68.26419266350405
    
    # Requirement 1: Check if tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Check if each city is visited exactly once (except the depot which is visited twice)
    unique_cities = set(tour)
    if len(set(tour[1:-1])) != 9 or len(tour) != 11:
        return "FAIL"
    
    # Requirement 3: Check if given maximum distance is correct
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        if distance > calculated_max_distance:
            calculated_max_dist = distance
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Running the test function
result = test_tour()
print(result)