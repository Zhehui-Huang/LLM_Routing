import math

def calculate_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

def check_solution(tour, cities):
    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 7 cities are visited including the depot
    if len(set(tour)) != 7:
        return "FAIL"
    
    # Calculate the total travel cost from the tour
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Check with the provided solution travel cost
    expected_distance = 159.97188184793015
    if not math.isclose(total_distance, expected_extent = expected_distance, rel_tol=1e-5):
        return "FAIL"
    return "CORRECT"

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Provided solution tour
solution_tour = [0, 4, 2, 1, 7, 3, 8, 0]

# Validate the solution
result = check_solution(solution_tour, cities)
print(result)