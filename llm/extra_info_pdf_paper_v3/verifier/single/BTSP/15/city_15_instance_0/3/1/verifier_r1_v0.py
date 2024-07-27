import math

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def validate_tour(cities, tour, total_cost, max_distance):
    # Check Requirement 1: Start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: All cities visited exactly once, except depot city 0
    all_cities = list(range(len(cities)))
    if sorted(tour[:-1]) != all_cities:
        return "FAIL"
    
    # Check Requirement 3: Accurate calculation of total travel cost and maximum distance
    computed_total_cost = 0
    computed_max_distance = 0
    for i in range(1, len(tour)):
        distance = euclidean_distance(cities[tour[i - 1]], cities[tour[i]])
        computed_total_cost += distance
        computed_max_adistance = max(computed_max_distance, distance)
    
    if not math.isclose(computed_total_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    if not math.isclose(computed_max_distance, max_distance, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Cities given by their coordinates
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
    (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Tour solution to test
tour_solution = [0, 8, 10, 1, 11, 14, 9, 4, 12, 7, 3, 5, 6, 2, 13, 0]
total_travel_cost = 373.97393412233544
max_distance_between_cities = 63.60031446463138

# Running the validation test
result = validate_tour(cities, tour_solution, total_travel_cost, max_distance_between_cities)
print(result)