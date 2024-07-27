import math

# Given cities and their positions
cities = {
    0: (84, 67),  # depot city
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

# Output from solver
tour = [0, 8, 3, 0]
total_travel_cost = 37.70721118904165
max_distance_between_cities = 18.027756377319946


def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, cities, total_travel_cost, max_distance_between_cities):
    # Check if tour begins and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check all cities are visited exactly once, except the depot
    visited = set(tour)
    if len(visited) != len(cities) or any(tour.count(city) != 1 for city in visited if city != 0):
        return "FAIL"

    # Calculate total travel cost from the tour
    calculated_cost = 0
    calculated_max_distance = 0
    
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_cost += dist
        if dist > calculated_max_distance:
            calculated_max_calc_distance = dist
            
    # Check if calculated cost and max distance match given values
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"
    if not math.isclose(calculated_max_distance, max_distance_between_cities, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Run verification
result = verify_solution(tour, cities, total_travel_no_cost, max_distance_between_cities)
print(result)