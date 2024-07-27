import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour_and_cost(tour, cost, city_coords, groups):
    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if the cost is calculated as the Euclidean distance
    calc_cost = 0
    for i in range(len(tour) - 1):
        calc_cost += euclidean_distance(city_coords[tour[i]], city_coords[tour[i + 1]])
    if not math.isclose(calc_cost, cost, rel_tol=1e-2):
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    visited_groups = [0 for _ in groups]
    for city in tour[1:-1]:  # exclude the depot city from the check
        for i in range(len(groups)):
            if city in groups[i]:
                visited_groups[i] += 1
    if any(v != 1 for v in visited_groups):
        return "FAIL"
    
    return "CORRECT"

# City coordinates, with index corresponding to city number
city_coords = [
    (54, 87),  # Depot city 0
    (21, 84),  # City 1
    (69, 84),  # City 2
    (53, 40),  # City 3
    (54, 42),  # City 4
    (36, 30),  # City 5
    (52, 82),  # City 6
    (93, 44),  # City 7
    (21, 78),  # City 8
    (68, 14),  # City 9
    (51, 28),  # City 10
    (44, 79),  # City 11
    (56, 58),  # City 12
    (72, 43),  # City 13
    (6, 99)    # City 14
]

# Groups of cities
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Solution provided
provided_tour = [0, 12, 10, 4, 3, 2, 0]
provided_cost = 138.15

# Check provided solution
print(verify_tour_and_cost(provided_tour, provided_cost, city_coords, groups))