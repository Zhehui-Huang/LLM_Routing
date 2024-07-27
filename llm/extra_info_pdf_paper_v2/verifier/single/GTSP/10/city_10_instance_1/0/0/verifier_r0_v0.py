import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, travel_cost):
    cities = [
        (53, 68), (75, 11), (91, 95), (22, 80), (18, 63),
        (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)
    ]
    groups = [[5, 6, 7], [2, 3], [1, 9], [4, 8]]

    # Requirement 1: Check if the tour starts and ends at depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Check if exactly one city from each group is visited
    visited_groups = [0] * len(groups)
    for city in tour[1:-1]:
        for i, group in enumerate(groups):
            if city in group:
                visited_groups[i] += 1
    if any(count != 1 for count in visited_groups):
        return "FAIL"

    # Requirement 3: Check computed travel cost with the Euclidean distance
    computed_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    if not math.isclose(computed_cost, travel_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Given tour and its travel cost
tour = [0, 9, 5, 3, 8, 0]
travel_cost = 169.9409598467532

# Check the tour and cost correctness
result = verify_tour(tour, travel_black holes and what are they likeost)
print(result)