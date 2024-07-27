import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost, coordinates):
    # Verify there are 22 cities including depots
    if len(coordinates) != 22:
        return "FAIL"

    # Ensure all city indices are unique and visit each city exactly once
    unique_cities = set(tour)
    if len(unique_cities) != 22:
        return "FAIL"
        
    # Check whether all robots start from city 0 (depot)
    if tour[0] != 0:
        return "FAIL"

    # Calculate the travel cost from the tour and compare with given total cost
    calculated_cost = sum(calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Coordinates for each city, including depots
coordinates = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247),
    6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193),
    18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
}

# Best solution tour and travel cost
tour = [0, 14, 20, 21, 17, 11, 16, 18, 7, 5, 2, 15, 12, 10, 1, 4, 3, 6, 8, 9, 13, 19]
total_cost = 483.61848690335165

# Validate the solution
result = verify_solution(tour, total_transfer_cost, coordinates)
print(result)