import math

def compute_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tours, costs, cities_coordinates, num_robots):
    # Verify number of cities
    if len(cities_coordinates) != 19:
        return "FAIL"

    # Check start and end at the depot
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

    # Set to collect visited cities
    visited_cities = set()

    # Verify that each city is visited exactly once and calculate costs
    computed_costs = []
    for robot_id in range(num_robots):
        tour = tours[robot_id]
        cost = 0
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i + 1]
            # Add city to set
            if city_to != 0:
                if city_to in visited_cities:
                    return "FAIL"
                visited_cities.add(city_to)
            # Calculate distance
            cost += compute_euclidean_distance(*cities_coordinates[city_from], *cities_coordinates[city_to])
        computed_costs.append(cost)

        # Check computed cost against provided cost
        if not math.isclose(cost, costs[robot_id], rel_tol=1e-5):
            return "FAIL"

    # All cities except the depot must be visited once
    if len(visited_cities) != 18:
        return "FAIL"

    # Check primary objective
    if max(computed_costs) != max(costs):
        return "FAIL"

    return "CORRECT"

# City coordinates including depot
cities_coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Provided solution
tours = [
    [0, 6, 5, 2, 7, 9, 13, 15, 18, 0],
    [0, 1, 3, 4, 14, 12, 11, 10, 8, 16, 17, 0]
]
costs = [103.11185888535181, 176.49212636224084]

# Number of robots
num_robots = 2

# Verify the solution
result = verify_solution(tours, costs, cities_coordinates, num_robots)
print(result)  # Should output "CORRECT" if the solution meets all requirements