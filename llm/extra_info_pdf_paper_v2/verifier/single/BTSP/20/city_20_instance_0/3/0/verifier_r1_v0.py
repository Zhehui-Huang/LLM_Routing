import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

cities = [
    (8, 11),  # City 0
    (40, 6),  # City 1
    (95, 33),  # City 2
    (80, 60),  # City 3
    (25, 18),  # City 4
    (67, 23),  # City 5
    (97, 32),  # City 6
    (25, 71),  # City 7
    (61, 16),  # City 8
    (27, 91),  # City 9
    (91, 46),  # City 10
    (40, 87),  # City 11
    (20, 97),  # City 12
    (61, 25),  # City 13
    (5, 59),  # City 14
    (62, 88),  # City 15
    (13, 43),  # City 16
    (61, 28),  # City 17
    (60, 63),  # City 18
    (93, 15)   # City 19
]

# Provided solution
tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
total_travel_cost = 349.20
max_distance = 32.39

# Validate the tour starts and ends at the depot city 0
def test_start_end_depot():
    return tour[0] == 0 and tour[-1] == 0

# Validate that each city is visited exactly once except the depot
def test_visit_each_city_once():
    visits = sorted(tour[:-1])  # exclude the last depot visit for this check
    return visits == list(range(len(cities)))

# Validate the provided maximum distance
def test_max_distance():
    max_distance_calculated = max(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    return math.isclose(max_distance_calculated, max_distance, rel_tol=1e-2)

# Validate the total travel cost
def test_total_travel_cost():
    total_cost_calculated = sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    return math.isclose(total_cost_calculated, total_travel_cost, rel_tol=1e-2)

# Run tests
if all([test_start_end_de-sup(), test_visit_each_city_once(), test_max_distance(), test_total_travel_cost()]):
    print("CORRECT") 
else:
    print("FAIL")