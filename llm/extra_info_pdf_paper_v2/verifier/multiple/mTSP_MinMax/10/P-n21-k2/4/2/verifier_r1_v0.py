import math

def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tours_and_costs(robot_tours, travel_costs, city_coords):
    visited_cities = set()
    all_cities = set(range(1, 21))  # Cities 1-20 should be visited
    max_travel_cost_reported = max(travel_costs)

    for robot_id, tour in enumerate(robot_tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # Tours must start and end at depot city 0
        tour_costs = 0
        previous_city = tour[0]
        for city in tour[1:]:
            if city != 0:  # Avoid counting the depot when revisiting within tour
                visited_cities.add(city)
            tour_costs += calculate_distance(city_coords[previous_city], city_coords[city])
            previous_city = city
        if travel_costs[robot_id] != round(tour_costs):
            return "FAIL"  # Reported travel cost must match the calculated cost

    if visited_cities != all_cities:
        return "FAIL"  # Every city except the depot must be visited exactly once

    if max(travel_costs) != max_travel_cost_reported:
        return "FAIL"  # Max travel cost must be correctly reported

    return "CORRECT"

# City coordinates array
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

# Tours submitted as per solution
robot_0_tour = [0, 16, 1, 10, 12, 15, 4, 11, 3, 0]
robot_1_tour = [0, 8, 18, 19, 13, 9, 17, 14, 5, 20, 6, 7, 2, 0]

# Total travel cost submitted
robot_0_cost = 113
robot_1_cost = 119

robot_tours = [robot_0_tour, robot_1_tour]
travel_costs = [robot_0_cost, robot_1_cost]

# Verify the solution using the function
print(verify_tours_and_costs(robot_tours, travel_costs, coordinates))