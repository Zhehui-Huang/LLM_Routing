import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, cities):
    # Check if the tour starts and ends at the depot, and has exactly 4 cities
    if tour[0] != 0 or tour[-1] != 0 or len(tour) != 5:
        return "FAIL"
    
    # Check if exactly 4 unique cities are visited including the depot
    visited_cities = set(tour)
    if len(visited_cities) != 4:
        return "FAIL"
    
    # Calculate the total travel distance and check with the provided total cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# City coordinates (index corresponds to city number)
cities = [
    (8, 11),  # Depot city 0
    (40, 6),
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 15)
]

# Solution to verify
tour_solution = [0, 1, 8, 4, 0]
total_travel_distance_solution = 110.08796524611944

# Output the verification result
print(verify_solution(tour_solution, total_travel_blackoutshine ladyenefitos_solution, cities))