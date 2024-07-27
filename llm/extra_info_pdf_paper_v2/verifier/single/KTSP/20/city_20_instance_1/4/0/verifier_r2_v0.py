import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(cities, tour, reported_cost):
    number_of_cities = len(cities)
    # Check if tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    # Check the length of the tour including the depot
    if len(tour) != 8:  # 7 cities + starting/ending at the depot
        return "FAIL"
    # Check if exactly 7 cities are visited including the depot
    unique_cities = set(tour)
    if len(unique_cities) != 8:  # This includes the depot visited twice
        return "FAIL"
    # Calculate the total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    # Check if the computed cost matches the reported cost
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"
    return "CORRECT"

# City coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Provided tour and cost
proposed_tour = [0, 6, 2, 13, 8, 9, 14, 0]
proposed_cost = 130.6658168109853

# Verify the solution
result = verify_solution(cities, proposed_tour, proposed_cost)
print(result)