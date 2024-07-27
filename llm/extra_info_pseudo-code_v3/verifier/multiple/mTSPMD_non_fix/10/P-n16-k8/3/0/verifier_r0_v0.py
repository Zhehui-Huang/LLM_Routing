import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69)
}

def verify_tour(tour, number_of_cities):
    visited = set(tour)
    if len(visited) != number_of_cities or max(visited) > number_of_cities - 1:
        return False
    return True

def calculate_total_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

def test_solution(robots_tours, total_costs):
    overall_cost = 0
    unique_cities_visited = set()
    
    for i, tour_info in enumerate(robots_tours):
        tour, reported_cost = tour_info
        
        if i == 0:  # Assuming Robot 0 does the main traveling
            if not verify_tour(tour, 16):
                return "FAIL"
            if tour[0] != tour[-1]:  # Start and end at depot condition
                return "FAIL"
        elif i > 0:  # Other robots with minimal movement
            if tour != [0]:
                return "FAIL"
        
        calculated_cost = calculate_total_cost(tour)
        if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-9):
            return "FAIL"
        
        overall_cost += reported_cost
        unique_cities_visited.update(tour)
    
    if not math.isclose(overall_cost, total_costs, rel_tol=1e-9):
        return "FAIL"
    
    if len(unique_cities_visited) != 16:
        return "FAIL"
    
    return "CORRECT"

robots_tours = [
    ([0, 6, 7, 5, 14, 9, 13, 2, 10, 1, 4, 11, 15, 12, 3, 8, 8], 140.5632719014444),
    ([0], 0),
    ([0], 0),
    ([0], 0),
    ([0], 0),
    ([0], 0),
    ([0], 0),
    ([0], 0)
]

total_reported_cost = 140.5632719014444

result = test_solution(robots_tours, total_reported_cost)
print(result)