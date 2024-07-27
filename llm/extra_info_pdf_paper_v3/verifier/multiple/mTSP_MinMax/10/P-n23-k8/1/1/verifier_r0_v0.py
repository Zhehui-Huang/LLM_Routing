import math

# Given solution tours and tour costs
solution_tours = [
    [0, 2, 8, 13, 9, 0],
    [0, 3, 12, 15, 0],
    [0, 6, 21, 0],
    [0, 14, 17, 0],
    [0, 1, 10, 16, 0],
    [0, 18, 19, 0],
    [0, 4, 11, 0],
    [0, 20, 5, 22, 7, 0]
]

tour_costs = [
    82.38880787623259,
    78.20189727339391,
    24.475701583477655,
    69.35939917750704,
    42.6682117120349,
    89.42264879375188,
    57.394073777130664,
    56.427922234652414
]

cities = [
    (30, 40),  # depot
    (37, 52),
    (49, 49),
    (52, 64),
    (31, 62),
    (52, 33),
    (42, 41),
    (52, 41),
    (57, 58),
    (62, 42),
    (42, 57),
    (27, 68),
    (43, 67),
    (58, 48),
    (58, 27),
    (37, 69),
    (38, 46),
    (61, 33),
    (62, 63),
    (63, 69),
    (45, 35),
    (32, 39),
    (56, 37)
]

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def verify_tours(tours, cities, costs):
    all_cities_visited = set(range(1, len(cities)))  # exclude the depot city

    def verify_tours_and_costs():
        calculated_costs = []
        for tour in tours:
            # Check if each tour starts and ends at the depot
            if tour[0] != 0 or tour[-1] != 0:
                return False, "Tour must start and end at depot"
            tour_cost = 0
            for i in range(len(tour) - 1):
                tour_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
                if i != 0:
                    all_cities_visited.discard(tour[i])
            calculated_costs.append(tour_cost)
        return calculated_costs

    calculated_costs = verify_tours_and_costs()
    
    # Verify all cities visited once
    if all_cities_visited:
        return False, "Not all cities are visited exactly once"

    # Verify costs closely
    for calculated_cost, reported_cost in zip(calculated_costs, costs):
        if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-5):
            return False, "Mismatch in calculated tour costs"
            
    # Verify maximum cost is as reported
    if not math.isclose(max(costs), max(calculated_costs), rel_tol=1e-5):
        return False, "Mismatch in reporting maximum travel cost"
    
    return True, ""

correct, error_message = verify_tours(solution_tours, cities, tour_costs)
if correct:
    print("CORRECT")
else:
    print("FAIL:", error_message)