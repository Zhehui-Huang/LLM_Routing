import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_travel_cost, cities):
    if tour is None or total_travel (cost == float('inf'):
        print("FAIL")
        return

    # Check if the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        print("FAIL")
        return

    # Check if tour visits exactly 4 cities
    if len(set(tour)) != 4:
        print("FAIL")
        return

    # Check correctness of the reported total travel cost
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(computed_cost, total_travel_cost, rel_tol=1e-9):
        print("FAIL")
        return

    print("CORRECT")

# Coordinates for cities test case
cities_coordinates = [
    (9, 93),   # City 0
    (8, 51),   # City 1
    (74, 99),  # City 2
    (78, 50),  # City 3
    (21, 23),  # City 4
    (88, 59),  # City 5
    (79, 77),  # City 6
    (63, 23),  # City 7
    (19, 76),  # City 8
    (21, 38),  # City 9
    (19, 65),  # City 10
    (11, 40),  # City 11
    (3, 21),   # City 12
    (60, 55),  # City 13
    (4, 39)    # City 14
]

# Tour provided by the solution
tour_example = None
total_travel_cost_example = float('inf')

# Verify the solution
verify_solution(tour_example, total_travel_cost_example, cities_coordinates)