import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

cities = [
    (8, 11),  (40, 6),  (95, 33), (80, 60), (25, 18), (67, 23),  (97, 32),
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25),
    (5, 59),  (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Provided solution
tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
total_travel_cost = 349.20
max_distance = 32.39

# Validate the tour starts and ends at the depot city 0
def test_start_end_at_depot():
    return tour[0] == 0 and tour[-1] == 0

# Validate that each city is visited exactly once except the depot
def test_visit_each_city_once():
    unique_visits = sorted(set(tour[:-1]))
    return unique_visits == list(range(len(cities)))

# Validate the provided maximum distance
def test_max_distance():
    calculated_max_distance = max(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    return math.isclose(calculated_max_distance, max_distance, rel_tol=1e-2)

# Validate the total travel cost
def test_total_travel_cost():
    calculated_total_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    return math.isclose(calculated_total_cost, total_travel_cost, rel_tol=1e-2)

# Execute tests
test_results = [
    test_start_end_at_depot(),
    test_visit_each_city_once(),
    test_max_distance(),
    test_total_travel_cost()
]

if all(test_results):
    print("CORRECT") 
else:
    print("FAIL")