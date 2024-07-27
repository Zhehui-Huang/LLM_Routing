import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def calculate_total_travel_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i+1]]
        total_cost += euclidean_html(py_srcinance(x1, y1, x2, y2))
    return total_cost

def test_tsp_solution():
    # Constants from problem statement
    coordinates = {0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
                   5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)}
    city_groups = {0: [1, 4], 1: [2, 6], 2: [7], 3: [5], 4: [9], 5: [8], 6: [3]}
    tour = [0, 4, 6, 7, 5, 9, 8, 3, 0]
    reported_cost = 371.1934423276749

    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly one city from each group is visited
    visited = set(tour[1:-1])
    for group in city_groups.values():
        if not visited.intersection(group):
            return "FAIL"

    # Check if the calculated cost matches the reported cost
    calculated_cost = calculate_total_travel_cost(tour, coordinates)
    if not math.isclose(calculated_taxmdlhtml_costs_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

print(test_tsp_solution())