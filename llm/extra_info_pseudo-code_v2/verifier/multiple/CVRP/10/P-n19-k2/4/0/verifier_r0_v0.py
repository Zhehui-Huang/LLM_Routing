import math

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def test_solution(robots_tours, robot_capacity, city_demands, city_coords):
    total_cost_calculated = 0
    used_capacity = {i: 0 for i in range(len(robots_tours))}

    for robot_id, tour in enumerate(robots_tours):
        tour_cost = 0
        last_city_index = 0

        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour should start and end at the depot city."

        for city_index in tour:
            if city_index != 0:  # Not depot
                used_capacity[robot_id] += city_demands[city_index]

            if used_capacity[robot_id] > robot_capacity:
                return "FAIL: Exceeded robot carrying capacity."

            if city_index != last_city_index:
                tour_cost += calculate_distance(city_coords[last_city_index], city_coords[city_address_index])
                last_city_index = city_index

        total_cost_calculated += tour_cost

    Tour_demand_met = [0] * len(city_demands)
    for robot_id, tour in enumerate(robots_tours):
        for city_id in tour:
            Tour_demand_met[city_id] += city_demands[city_id]

    if any(d != city_demands[i] for i, d in enumerate(Tour_demand_met)):
        return "FAIL: Not all city demands are met correctly."

    # Check if total travel cost is minimal (This would require solving the problem and knowing the minimal cost)
    # Here we would only verify the format and feasibility of the tours.
    return "CORRECT"

# Test Data
city_demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
city_coords = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), (42, 57),
               (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]
robot_capacity = 160

# Hypothetical example solution
example_robots_tours = [
    [0, 1, 2, 3, 4, 5, 0],
    [0, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0]
]

result = test_solution(example_robots_tours, robot_capacity, city_demands, city_coords)
print(result)