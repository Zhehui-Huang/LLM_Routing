import math

# City coordinates indexed by city ID
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

# Tours of all robots
robots_tours = [
    [0, 8, 0],
    [0, 1, 9, 0],
    [0, 2, 10, 0],
    [0, 3, 11, 0],
    [0, 4, 12, 0],
    [0, 5, 13, 0],
    [0, 6, 14, 0],
    [0, 7, 15, 0]
]

def calculate_total_travel_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = city_coordinates[tour[i]]
        x2, y2 = city_coordinates[tour[i + 1]]
        total_cost += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return total_cost

correct_tour_costs = [64.89992295835181, 72.88070710888512, 52.4625939010481, 86.03587467520119, 64.98936367308863, 68.36272673975597, 64.17258428512785, 83.62034367443502]

# Correctness checks
def test_solution_correctness():
    overall_total_cost = 0
    visited_cities = set()
    for i, tour in enumerate(robots_tours):
        # Verify visitation to each city exactly once and starts and ends at depot
        without_depot = [city for city in tour if city != 0]
        visited_cars = set(without_depot)
        if len(without_depot) != len(visited_cars):
            return "FAIL"
        visited_cities.update(visited_cars)
        
        # Verify total travel cost for each robot
        tour_cost = calculate_total_travel_cost(tour)
        if not math.isclose(tour_cost, correct_tour_costs[i], rel_tol=1e-9):
            print(f"Reported Cost: {correct_tour_costs[i]}, Calculated Cost: {tour_cost}")
            return "FAIL"
        overall_total_cost += tour_cost

    # Ensure all cities are visited exactly once
    if visited_cities != set(range(1, 16)):  # cities 1 to 15
        return "FAIL"
        
    # Verify overall cost
    reported_total_cost = 557.4241170158938
    if not math.isclose(overall_total_cost, reported_total_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Run the test function
result = test_solution_correctness()
print(result)