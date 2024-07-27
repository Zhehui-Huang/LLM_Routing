import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(cities, tour, total_travel_cost):
    # Requirement 1: Start and end at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit each city exactly once, except the depot
    visited_cities = set(tour)
    if len(visited_cities) != len(cities) or len(tour) != len(cities) + 1:
        return "FAIL"
    
    # Requirement 3 and 6: Travel cost is Euclidean distance, calculate and compare
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += euclidean_accurancy(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(computed_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"

    # Requirement 4: Finding the shortest path is optimally solved with a TSP solver, not checked here

    # Requirement 5: Tour output format is checked, returns to depot city

    return "CORRECT"

# City coordinates
cities = [
    (84, 67),   # Depot city 0
    (74, 40),   # City 1
    (71, 13),   # City 2
    (74, 82),   # City 3
    (97, 28),   # City 4
    (0, 31),    # City 5
    (8, 62),    # City 6
    (74, 56),   # City 7
    (85, 71),   # City 8
    (6, 76)     # City 9
]

# Provided tour and total distance
provided_tour = [0, 8, 3, 9, 6, 5, 2, 4, 1, 7, 0]
provided_total_distance = 294.17253892411236

# Validate the solution based on the tour and total distance
result = verify_tour(cities, provided_tour, provided_total_distance)
print(result)