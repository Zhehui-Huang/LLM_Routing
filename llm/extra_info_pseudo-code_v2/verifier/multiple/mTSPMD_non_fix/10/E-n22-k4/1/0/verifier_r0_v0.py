import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_requirements(tour, coordinates, expected_cost):
    if len(set(tour)) != len(tour):
        return "FAIL - Cities are repeated in the tour."
    if sorted(tour) != list(range(len(coordinates))):
        return "FAIL - Not all cities are covered."
    if tour[0] != 0:
        return "FAIL - Tour does not start at the designated starting depot."

    total_cost = 0
    for i in range(1, len(tour)):
        city1 = tour[i-1]
        city2 = tour[i]
        x1, y1 = coordinates[city1]
        x2, y2 = coordinates[city2]
        total_cost += calculate_euclidean_distance(x1, y1, x2, y2)

    if abs(total_cost - expected_cost) > 1e-5:
        return f"FAIL - Total travel cost mismatch. Expected: {expected_cost}, Calculated: {total_cost}"

    return "CORRECT"

# Define the coordinates of the cities as given in the problem
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Define the tour obtained (solution provided)
optimal_tour = [0, 1, 2, 5, 6, 4, 3, 11, 13, 10, 8, 7, 9, 12, 17, 19, 16, 14, 15, 18, 20, 21]
total_travel_cost = 364.20363969798024

# Invoke the verification function
result = check_requirements(optimal_tour, coordinates, total_travel_cost)
print(result)