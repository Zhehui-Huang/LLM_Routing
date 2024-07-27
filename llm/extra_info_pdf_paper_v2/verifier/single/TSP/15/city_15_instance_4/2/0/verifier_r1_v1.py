import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tsp_solution(cities, tour, reported_cost):
    # Extract the requirements based on the constraints
    start_end_depot = tour[0] == 0 and tour[-1] == 0  # Start and end at the depot city (City 0)
    all_cities_visited_once = len(set(tour[1:-1])) == len(tour[1:-1]) == len(cities) - 1  # All cities visited exactly once except depot
    correct_tour_format = isinstance(tour, list) and all(isinstance(city, int) for city in tour)  # Tour format as a list of integers
    
    # Calculating the total distance of the given tour for verification
    total_distance = 0
    for i in range(1, len(tour)):
        city1 = tour[i-1]
        city2 = tour[i]
        total_distance += calculate_euclidean_distance(cities[city1][0], cities[city1][1], cities[city2][0], cities[city2][1])
    
    correct_total_distance = math.isclose(total_distance, reported_cost, rel_tol=1e-9)  # Check if computed and reported costs are close
    
    # Return "CORRECT" if all requirements are met, otherwise "FAIL"
    if all([start_end_depot, all_cities_visited_once, correct_total_distance, correct_tour_format]):
        return "CORRECT"
    else:
:
        return "FAIL"

# Cities coordinates including depot city at index 0
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), 
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44), 
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Provided solution tour and cost
solution_tour = [0, 1, 5, 9, 2, 7, 4, 12, 11, 6, 3, 8, 14, 13, 10, 0]
solution_cost = 288.5242816725832

# Checking the provided solution
result = verify_tsp_solution(cities, solution_tour, solution_cost)
print(result)