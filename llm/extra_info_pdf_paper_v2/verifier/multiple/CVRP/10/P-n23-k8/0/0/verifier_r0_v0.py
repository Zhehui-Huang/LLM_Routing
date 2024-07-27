import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_tour_cost(tour, coordinates):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(*coordinates[tour[i]], *coordinates[tour[i+1]])
    return cost

def test_solution(tours, demands, capacities, coordinates):
    all_tours = []
    overall_cost_calculated = 0
    total_demand_met = [0] * len(demands)

    # Check all tours and calculate their cost
    for i, tour in enumerate(tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour must start and end at the depot (city 0)"

        # Calculate tour cost
        tour_cost = calculate_tour_cost(tour, coordinates)
        overall_cost_calculated += tour_cost
        
        # Check capacity constraint
        current_load = 0
        for city in tour[1:-1]:
            current_load += demands[city]
            total_demand_met[city] += demands[city]
        if current_load > capacities[i]:
            return f"FAIL: Capacity exceeded for robot {i}"
            
        all_tours.append({"tour": tour, "tour_cost": tour_cost})

    # Check demands are correctly met
    if any(d != demands[idx] for idx, d in enumerate(total_demand_met) if idx != 0):
        return "FAIL: Demands not met correctly"

    # Check overall total travel cost verification (implied correctness via individual costs)
    reported_total_cost = sum(tour_data["tour_cost"] for tour_data in all_tours)
    if not math.isclose(overall_cost_calculated, reported_total_cost):
        return "FAIL: Reported total travel cost does not match calculated cost"

    return "CORRECT"

# Define the tours and data as provided above
tours = [
    [0, 18, 19, 0],
    [0, 9, 17, 0],
    [0, 12, 15, 0],
    [0, 8, 13, 0],
    [0, 14, 22, 0],
    [0, 4, 11, 0],
    [0, 3, 10, 0],
    [0, 5, 7, 0]
]

demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
capacities = [40] * 8
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

# Execute test
test_result = test_solution(tours, demands, capacities, coordinates)
print(test_result)