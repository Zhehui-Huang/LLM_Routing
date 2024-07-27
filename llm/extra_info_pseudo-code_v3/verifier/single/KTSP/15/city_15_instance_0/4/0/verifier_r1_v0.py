import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def check_tour_cities_count(tour, expected_count):
    return len(set(tour)) == expected_count

def check_tour_start_end(tour, depot):
    return tour[0] == depot and tour[-1] == depot

def calculate_total_tour_cost(tour, city_positions):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(city_positions[tour[i]], city_positions[tour[i+1]])
    return total_cost

def conduct_unit_tests(tour, expected_cost, city_positions):
    depot = 0
    required_cities_including_depot = 4

    # Test the tour for the number of unique cities including the depot
    if not check_tour_cities_count(tour, required_cities_including_depot):
        return "FAIL"

    # Depo as start and end
    if not check_tour_start_end(tour, depot):
        return "FAIL"
    
    # Calculate and check distance
    calculated_cost = calculate_total_tour_cost(tour, city_positions)
    if not math.isclose(calculated_cost, expected_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# City coordinates mapping from the problem statement
city_positions = [
    (9, 93),   # Depot
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# Provided tour and total cost
proposed_tour = [0, 1, 10, 8, 0]
proposed_cost = 90.53947981328088

# Invoke the testing function
result = conduct_unit_tests(proposed_tour, proposed_cost, city_positions)
print(result)