import math

# Provided solution
tour_solution = [0, 8, 3, 9, 6, 5, 2, 4, 1, 7, 0]
total_travel_cost_solution = 294.17253892411236

# Cities coordinates
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

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_requirements(tour, total_cost):
    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit all cities exactly once except the depot
    cities_visited = set(tour[1:-1])
    if len(tour[1:-1]) != len(cities_visited) or len(cities_visited) != len(cities) - 1:
        return "FAIL"
    
    # Requirement 3: Calculate travel cost and compare
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(cities[city1][0], cities[city1][1], 
                                                        cities[city2][0], cities[city2][1])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Test the solution
result = verify_requirements(tour_solution, total_travel_cost_solution)
print(result)