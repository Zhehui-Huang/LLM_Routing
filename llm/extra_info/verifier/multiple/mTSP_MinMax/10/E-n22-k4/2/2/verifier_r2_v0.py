import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def compute_tour_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return round(total_cost, 2)

def test_solution():
    coordinates = [
        (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
        (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
        (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
        (164, 193), (129, 189), (155, 185), (139, 182)
    ]
    
    tours = [
        [0, 14, 16, 17, 20, 18, 0],
        [0, 15, 12, 10, 8, 6, 0],
        [0, 7, 5, 9, 2, 1, 0],
        [0, 3, 4, 11, 13, 19, 21, 0]
    ]
    
    provided_costs = [79.20, 97.59, 131.00, 171.71]
    maximum_cost = 171.71
    
    all_cities_included = set(range(1, 22))
    cities_visited = set()

    # Validate the solution
    for tour in tours:
        assert tour[0] == 0 and tour[-1] == 0, "Tours must start and end at the depot city."
        for city in tour[1:-1]:
            assert city not in cities_visited, "Each city must be visited exactly once."
            cities_visited.add(city)

    assert cities_visited == all_cities_included, "All cities must be visited exactly once."
    
    calculated_costs = [compute_tour_cost(tour, coordinates) for tour in tours]
    assert provided_costs == calculated_costs, "Provided travel costs must match calculated costs."
    
    assert max(provided_costs) == maximum_cost, "Maximum cost must match provided maximum cost."

    print("CORRECT")

try:
    test_solution()
except AssertionError as e:
    print("FAIL:", e)