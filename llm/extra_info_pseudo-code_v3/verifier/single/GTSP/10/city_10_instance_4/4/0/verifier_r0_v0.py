import math

# Provided cities and their coordinates
cities = {
    0: (79, 15),  # depot
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

# Groups of cities
city_groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Tour solution
tour = [0, 4, 6, 7, 5, 9, 8, 3, 0]
reported_total_cost = 371.19

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, city_groups, reported_cost):
    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculate actual total distance
    actual_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    
    # Check if cost matches
    if not math.isclose(actual_cost, reported_cost, abs_tol=0.01):
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    cities_in_tour = tour[1:-1]  # Exclude the starting and ending depot
    visited_groups = []

    for group in city_groups:
        # Check if exactly one city from each group is in the tour
        if sum(city in cities_in_tour for city in group) != 1:
            return "FAIL"

    return "CORRECT"

# Running the verification function
result = verify_tour(tour, city_groups, reported_total_cost)
print(result)