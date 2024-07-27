import math

coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246),
    (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214),
    (146, 208), (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), (139, 185)
]

demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300,
    300, 900, 2100, 1000, 900, 2500, 1800, 700
]

robot_tours = [
    [0, 14, 17, 20, 10, 5, 0],  # Robot 0
    [0, 16, 19, 21, 9, 0],      # Robot 1
    [0, 12, 15, 18, 7, 2, 1, 0],# Robot 2
    [0, 13, 11, 8, 6, 3, 4, 0]  # Robot 3
]

max_capacity = 6000

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def test_solution():
    total_demand_met = [0] * 22
    total_cost_calculated = 0

    for tour in robot_tours:
        last_city = tour[0]
        current_capacity_used = 0
        tour_cost = 0
        
        for idx in range(1, len(tour)):
            city = tour[idx]
            current_capacity_used += demands[city]
            distance = euclidean_distance(coordinates[last_city], coordinates[city])
            tour_cost += distance
            last_city = city
        
        if current_capacity_used > max_capacity:
            return "FAIL: Capacity exceeded."
        
        total_cost_calculated += tour_cost
        total_demand_met = [x + y for x, y in zip(total_demand_met, [demands[i] for i in tour])]

    if any(t != d for t, d in zip(total_demand_met, demands)):
        return "FAIL: Demands not met correctly."

    expected_costs = [138.8648131082581, 129.6158456468699, 164.3286424094758, 118.6828962404526]
    total_expected_cost = sum(expected_ges_costs)

    if not math.isclose(total_cost_calculated, total_expected_cost, rel_tol=1e-3):
        return f"FAIL: Costs do not match. Expected: {total_expected_cost}, Got: {total_cost_calculated}"

    return "CORRECT"

print(test_solution())