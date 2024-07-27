import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost):
    city_coordinates = {
        0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
        5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
        10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
        15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
    }

    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly 16 distinct cities are visited
    unique_cities = set(tour)
    if len(unique_cities) != 16:
        return "FAIL"

    # Ensure all cities in the tour are from the specified coordinates
    if any(city not in city_coordinates for city in unique_cities):
        return "FAIL"
    
    # Calculate and verify the total travel cost
    computed_cost = 0
    for i in range(len(tour)-1):
        computed_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])

    # Check computed cost closely matches the provided total travel cost
    if not math.isclose(computed_cost, total_cost, abs_tol=1e-6):
        return "FAIL"
    
    return "CORRECT"

# Provided tour and total travel cost
tour = [0, 19, 1, 11, 14, 9, 10, 15, 4, 3, 6, 7, 16, 5, 17, 8, 0]
total_cost = 378.00

# Execute the verification
test_result = verify_solution(tour, total_cost)
print(test_result)