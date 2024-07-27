import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tours, costs, cities):
    # Cities coordinates {city_index: (x, y)}
    cities_coordinates = {
        0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
        5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
        10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
        15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
        20: (155, 185), 21: (139, 182)
    }

    all_cities_visited = set()
    calculated_costs = []
    total_calculated_cost = 0

    # Check each tour
    for tour, reported_cost in zip(tours, costs):
        if tour[0] != 0 or tour[-1] != 0:
            return False, "Tours must start and end at the depot (City 0)."

        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]])
            all_cities_visited.add(tour[i])

        calculated_costs.append(round(tour_cost, 2))
        total_calculated_cost += tour_cost
        if not math.isclose(tour_cost, reported_cost, abs_tol=0.01):
            return False, f"Reported cost {reported_cost} does not match calculated cost {tour_cost} for tour."

    if len(all_cities_visited) != len(cities_coordinates):
        return False, "Not all cities have been visited exactly once collectively."

    if not math.isclose(sum(costs), total_calculated_cost, abs_tol=0.01):
        return False, f"Total reported cost {sum(costs)} does not match total calculated cost {total_calculated_cost}."

    return True, "CORRECT"

# Given solution data
tours = [
    [0, 16, 12, 8, 4, 20, 0],
    [0, 13, 17, 21, 9, 5, 1, 0],
    [0, 14, 18, 10, 6, 2, 0],
    [0, 15, 7, 3, 11, 19, 0]
]
costs = [177.49, 197.56, 154.73, 183.25]

# Verify the solution correctness
result, message = verify_solution(tours, costs, cities = list(range(22)))

if result:
    print("CORRECT")
else:
    print("FAIL:", message)