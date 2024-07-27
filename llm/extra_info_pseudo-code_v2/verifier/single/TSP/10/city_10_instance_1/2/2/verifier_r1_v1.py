import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_travel_cost(tour, cities):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))

def is_tour_correct(tour, expected_cost, cities):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start and end at the depot city."
    if len(set(tour[1:-1])) != len(cities) - 1:
        return "FAIL: Tour does not visit all cities exactly once and only once."
    if sorted(tour[1:-1]) != list(range(1, len(cities))):
        return "FAIL: Tour does not visit all non-depot cities."
    calculated_cost = round(total_travel_cost(tour, cities), 2)
    if calculated_cost != expected_cost:
        return f"FAIL: Incorrect total travel cost calculated. Expected: {expected_cost}, Got: {calculated_cost}"
    return "CORRECT"

# Constants and input data
CITIES = [
    (53, 68),  # Depot city 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

TOUR = [0, 4, 8, 3, 5, 2, 9, 7, 1, 6, 0]
EXPECTED_COST = 278.93

# Check the tour
result = is_tour_correct(TOUR, EXPECTED_COST, CITIES)
print(result)