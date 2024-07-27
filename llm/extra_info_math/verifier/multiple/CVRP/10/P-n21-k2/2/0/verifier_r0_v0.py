import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def test_solution():
    # Provided solution data
    robots_tours = [
        [0, 6, 0],
        [0, 16, 0]
    ]
    robots_travel_costs = [24.08, 20.00]
    total_travel_cost = 44.08
    
    # Test data
    city_coordinates = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
        15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
        20: (45, 35)
    }
    demands = {
        1: 7, 2: 30, 3: 16, 4: 23, 5: 11, 6: 19, 7: 15, 8: 28,
        9: 8, 10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11, 16: 12,
        17: 26, 18: 17, 19: 6, 20: 15
    }
    robot_capacity = 160
    total_cities = len(city_coordinates) - 1 # excluding depot

    visited_cities = set()
    calc_total_cost = 0

    for tour, reported_cost in zip(robots_tours, robots_travel_costs):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Route must start and end at the depot"
        load = 0
        calc_cost = 0
        for i in range(len(tour)-1):
            from_city, to_city = tour[i], tour[i+1]
            visited_cities.add(from_city)
            visited_cities.add(to_city)
            distance = calculate_euclidean_distance(city_coordinates[from_city], city_coordinates[to_city])
            calc_cost += distance
            if from_city != 0:  # Don't add depot's demand
                load += demands[from_city]
        if load > robot_capacity:
            return "FAIL: Capacity exceeded"
        if abs(calc_cost - reported_cost) > 1e-2:  # rounding leeway due to floating point arithmetic
            return f"FAIL: Incorrect reported travel cost {reported_cost} vs {calc_cost}"

        calc_total_cost += calc_cost

    if len(visited_cities) != total_cities + 1:  # including depot
        return "FAIL: Not all cities visited exactly once"

    if abs(calc_total_cost - total_travel_cost) > 1e-2:
        return f"FAIL: Incorrect total travel cost {total_travel_cost} vs {calc_total_cost}"

    return "CORRECT"

# Running the test
print(test_solution())