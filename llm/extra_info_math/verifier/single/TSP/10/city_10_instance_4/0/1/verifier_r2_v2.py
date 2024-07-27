import math

# List of city coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Tour provided as solution
tour = [0, 3, 6, 2, 8, 9, 1, 5, 7, 4, 0]
# Reported total cost of the tour
reported_total_cost = 320.7939094250147

# Compute Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Validate starting and ending at the depot (city 0)
def check_start_end(tour):
    return tour[0] == 0 and tour[-1] == 0

# Check if all cities are visited exactly once
def check_all_visited_once(tour):
    unique_cities_visited = set(tour)
    all_cities = set(cities.keys())
    return unique_cities_visited == all_cities and all(tour.count(x) == 1 for x in unique_cities_visited if x != 0)

# Check if the calculated travel cost matches the reported total cost
def check_total_cost(tour, reported_total_cost):
    calculated_total_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    return math.isclose(calculated_total_cost, reported_total_cost, rel_tol=1e-9)

# Validation function to verify all constraints
def validate_solution(tour, reported_total_cost):
    if not check_start_end(tour):
        return "FAIL"
    if not check_all_visited_once(tour):
        return "FAIL"
    if not check_total_cost(tour, reported_total_cost):
        return "FAIL"
    return "CORRECT"

# Execute the validation and print the result
output = validate_secretion(tour, reported_total_cost)
print(output)