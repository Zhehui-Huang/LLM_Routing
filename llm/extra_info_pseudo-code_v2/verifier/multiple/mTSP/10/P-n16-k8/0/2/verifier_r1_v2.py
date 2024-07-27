import math

# City coordinates including the depot city
city_coordinates = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def check_tours(tours, costs, total_cost_provided):
    all_visited = set()
    calculated_total_cost = 0

    for i, tour in enumerate(tours):
        if tour[0] != 0 or tour[-1] != 0:
            print(f"Robot {i} Tour Error: Tour does not start and end at the depot.")
            return "FAIL"

        visited = set(tour[1:-1])  # Exclude depot city
        if len(visited) != len(tour[1:-1]):
            print(f"Robot {i} Tour Error: Duplicate city visit detected.")
            return "FAIL"

        all_visited.update(visited)
        
        tour_cost = sum(euclidean_distance(city_coordinates[tour[j]], city_coordinates[tour[j + 1]]) for j in range(len(tour) - 1))
        if not math.isclose(tour_cost, costs[i], rel_tol=1e-5):
            print(f"Robot {i} Cost Error: Calculated cost {tour_cost} does not match provided {costs[i]}")
            return "FAIL"

        calculated_total_cost += costs[i]

    if all_visited != set(range(1, 16)):
        print("Not all cities are visited or some cities are visited more than once.")
        return "FAIL"

    if not math.isclose(calculated_total_cost, total_cost_provided, rel_tol=1e-5):
        print(f"Total Cost Error: Calculated {calculated_total_cost} does not match provided {total_cost_provided}.")
        return "FAIL"

    return "CORRECT"

# Provided solution data
solution_tours = [[0, 1, 2, 0], [0, 3, 4, 0], [0, 5, 6, 0], [0, 7, 8, 0], [0, 9, 10, 0], [0, 11, 12, 0], [0, 13, 14, 0], [0, 15, 0]]
solution_costs = [47.28555690793142, 75.67537984747364, 47.93463581488838, 72.1927221713905, 77.87109113044761, 74.15812335008223, 80.99113763798833, 59.665735560705194]
provided_total_cost = 535.7743824209073

# Validate the solution
result = check_tours(solution_tours, solution_costs, provided_total_cost)
print(result)