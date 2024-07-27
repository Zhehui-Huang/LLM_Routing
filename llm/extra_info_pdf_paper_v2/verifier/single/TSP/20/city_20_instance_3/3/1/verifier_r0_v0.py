import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_solution(tour, cities, total_cost_reported):
    # [Requirement 1] Check number of cities
    if len(cities) != 20:
        return "FAIL"
    
    # [Requirement 2] Check depot city coordinates
    if cities[0] != (30, 56):
        return "FAIL"
    
    # [Requirement 3] Check tour starts and ends at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 4] Check all cities are visited exactly once excluding the depot at the end
    if sorted(tour[1:-1]) != list(range(1, 20)):
        return "FAIL"
    
    # [Requirement 5] Check if the total cost is calculated correctly using Euclidean distance
    total_cost_calculated = 0
    for i in range(len(tour) - 1):
        city_index1 = tour[i]
        city_index2 = tour[i+1]
        total_cost_calculated += calculate_distance(cities[city_index1], cities[city_index2])
    
    if not math.isclose(total_cost_calculated, total_cost_reported, rel_tol=1e-9):
        return "FAIL"
    
    # If all checks pass
    return "CORRECT"

# Cities coordinates (ID: coordinates)
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Tour provided
tour_provided = [0, 1, 18, 12, 7, 8, 14, 4, 10, 11, 9, 16, 17, 15, 5, 2, 13, 6, 19, 3, 0]
total_cost_provided = 450.7943736539333

# Verify the solution
result = check_solution(tour_provided, cities, total_cost_provided)
print(result)