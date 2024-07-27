import math

# City coordinates and demand list
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]
city_demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Robot tours and respective travel costs
robot_tours = [
    [0, 6, 0], [0, 1, 10, 13, 0], [0, 2, 0], [0, 4, 11, 0],
    [0, 7, 5, 9, 0], [0, 15, 12, 0], [0, 14, 3, 0], [0, 8, 0]
]
robot_costs = [24.08, 68.44, 42.05, 57.39, 75.54, 66.12, 100.91, 64.90]

# Constants
NUM_ROBOTS = 8
CAPACITY = 35


def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def verify_tour_starts_ends_at_depot(tour):
    return tour[0] == 0 and tour[-1] == 0


def verify_capacity(tour):
    used_capacity = sum(city_demands[city] for city in tour)
    return used_capacity <= CAPACITY


def verify_travel_costs(tour, reported_cost):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    return math.isclose(total_cost, reported_cost, rel_tol=1e-2)  # Allowing small floating-point error


def verify_demand_coverage(tours):
    demand_coverage = [0] * len(city_coordinates)
    for tour in tours:
        for city in tour:
            demand_coverage[city] += city_demands[city]
    demand_coverage[0] = 0  # Resetting depot's demand
    return all(dem == req for dem, req in zip(demand_coverage, city_demands))


def verify_solution(tours, costs):
    if not all(verify_tour_starts_ends_at_depot(tour) for tour in tours):
        return "FAIL: Tour does not start and end at the depot."

    if not verify_demand_coverage(tours):
        return "FAIL: Not all city demands are met."

    if not all(verify_capacity(tour) for tour in tours):
        return "FAIL: Capacity exceeded for one or more robots."

    for tour, cost in zip(tours, costs):
        if not verify_travel_costs(tour, cost):
            return "FAIL: Incorrect calculation of travel costs."

    return "CORRECT"


# Run the verification on the example solution.
result = verify_solution(robot_tours, robot_costs)
print(result)