import math

# Define the function to calculate Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Define the city coordinates
city_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Tours provided
robots_tours = [
    [0, 6, 13, 0],
    [0, 1, 15, 0],
    [0, 10, 12, 0],
    [0, 2, 14, 0],
    [0, 4, 9, 0],
    [0, 7, 8, 0],
    [0, 5, 3, 0],
    [0, 11, 0]
]

# Requirement 1: Check start/end at depot
def check_start_end_depot(tours):
    return all(tour[0] == 0 and tour[-1] == 0 for tour in tours)

# Requirement 2: Check all cities visited once
def check_all_cities_visited_once(tours, city_count):
    all_visited = set()
    for tour in tours:
        all_visited.update(tour[1:-1])  # Exclude the depot city from the visit list
    return all_visited == set(range(1, city_count))

# Requirement 3: Calculate distances and verify if presented correctly
def calculate_and_validate_distances(tours, reported_costs):
    calculated_costs = []
    for tour in tours:
        cost = 0
        for i in range(len(tour) - 1):
            cost += distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
        calculated_costs.append(cost)
    return all(math.isclose(calculated, reported, abs_tol=1e-5) for calculated, reported in zip(calculated_costs, reported_costs))


# The provided data
reported_costs = [
    58.62628333248735, 60.7253117698024, 60.8251757953491,
    75.66422277050432, 90.97688812070146, 72.1927221713905,
    86.6444339534298, 56.32051136131489
]
max_reported_cost = 90.97688812070146

# Checks
if (check_start_end_depot(robots_tours) and 
    check_all_cities_visited_once(robots_tours, 16) and
    calculate_and_validate_distances(robots_tours, reported_costs) and
    math.isclose(max(reported_costs), max_reported_cost, abs_tol=1e-5)):
    print("CORRECT")
else:
    print("FAIL")