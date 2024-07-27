import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour_and_cost(cities, tour, reported_cost):
    # Check if the tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if each city except the depot is visited exactly once
    visited = set(tour[1:-1])
    if len(visited) != len(cities) - 1 or any(city not in visited for city in range(1, len(cities))):
        return "FAIL"

    # Verify the cost calculation 
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = cities[tour[i]]
        city2 = cities[tour[i+1]]
        calculated_cost += calculate_euclidean_distance(city1[0], city1[1], city2[0], city2[1])
    
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Cities specified by their (x, y) coordinates
cities = [
    (3, 26),   # Depot city 0
    (85, 72),
    (67, 0),
    (50, 99),
    (61, 89),
    (91, 56),
    (2, 65),
    (38, 68),
    (3, 92),
    (59, 8),
    (30, 88),
    (30, 53),
    (11, 14),
    (52, 49),
    (18, 49),
    (64, 41),
    (28, 49),
    (91, 94),
    (51, 58),
    (30, 48)
]

tour = [0, 14, 6, 8, 10, 3, 4, 1, 17, 5, 9, 2, 15, 13, 18, 7, 11, 16, 19, 12, 0]
total_cost = 459.3756031617237

result = verify_tour_and_cost(cities, tour, total_cost)
print(result)