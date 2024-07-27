import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tsp_solution(cities, tour, reported_cost):
    # Validate the start and end at depot condition
    start_end_depot = tour[0] == 0 and tour[-1] == 0
    
    # Validate each city is visited exactly once, except depot
    unique_visits = set(tour[1:-1])
    all_cities_visited_once = len(unique_visits) == len(cities) - 1 and len(tour) - 1 == len(cities)
    
    # Calculate the total distance traveled and compare it against the reported cost
    total_distance = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        total_distance += calculate_euclidean_distance(*cities[city1], *cities[city2])
    
    correct_total_distance = math.isclose(total_distance, reported_cost, rel_tol=1e-9)

    # Result based on all conditions
    if all([start_end_depot, all_cities_visited_once, correct_total_distance]):
        return "CORRECT"
    else:
        return "FAIL"

# City coordinates including the depot city (index 0)
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Provided solution tour and their alleged cost
solution_tour = [0, 1, 5, 9, 2, 7, 4, 12, 11, 6, 3, 8, 14, 13, 10, 0]
solution_cost = 288.5242816725832

# Run the verification
result = verify_tsp_solution(cities, solution_tour, solution_cost)
print(result)  # Output the verification result, expected "CORRECT" or "FAIL"