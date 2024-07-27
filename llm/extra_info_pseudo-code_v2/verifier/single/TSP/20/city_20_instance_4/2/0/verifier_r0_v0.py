import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tour(cities, tour, expected_cost):
    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if tour covers all cities exactly once, except for the depot
    if sorted(tour) != sorted(list(range(len(cities)))):
        return "FAIL"
    
    # Calculate the total travel cost and check against the expected cost
    total_cost = 0.0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Use a tolerance for floating point comparison
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Cities coordinates (id corresponds to index)
cities_coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Provided solution details
tour_solution = [0, 10, 15, 4, 3, 6, 12, 7, 16, 9, 5, 2, 14, 11, 1, 13, 18, 17, 8, 19, 0]
total_cost_solution = 384.98718011848365

# Verify the solution
result = verify_tour(cities_coordinates, tour_solution, total_cost_solution)
print(result)