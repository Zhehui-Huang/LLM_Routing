import math

# Define the coordinates of each city
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Tours provided
tours = [
    [0, 11, 15, 8, 5, 7, 12, 0],
    [0, 3, 2, 18, 4, 6, 0],
    [0, 21, 16, 1, 20, 14, 0],
    [0, 9, 13, 17, 19, 10, 0]
]

# Provided travel costs
provided_costs = [168.61121672078318, 258.9072439288899, 227.3504115829129, 178.52658271678098]
max_cost_provided = 258.9072439288899

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

try:
    # Requirement 4: All cities, excluding the depot, must be visited exactly once
    all_cities_visited = set(city for tour in tours for city in tour if city != 0)
    assert len(all_cities_visited) == 21, "Not all cities are visited exactly once."

    # Requirement 3, 5 and 6: Calculate and check distances
    calculated_costs = []
    for tour in tours:
        cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        calculated_costs.append(cost)

    # Check maximum cost and individual tour costs
    max_calculated_cost = max(calculated_costs)
    assert all(math.isclose(provided, calculated, rel_tol=1e-5) for provided, calculated in zip(provided
                                    , calculated_costs)), "Mismatch in calculated tour costs"
    assert math.isclose(max_cost_provided, max_calculated_cost, rel_tol=1e-5), "Mismatch in maximum travel cost"

    print("CORRECT")

except AssertionError as e:
    print("FAIL:", str(e))