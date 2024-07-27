import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tours, costs, demands, robot_capacity, cities):
    total_demand_met = [0] * len(demands)
    total_capacity_used = [0] * len(tours)
    individual_costs = [0] * len(tours)
    all_visits = set()

    if not tours or not costs or not demands or robot_capacity <= 0 or not cities:
        return "FAIL"

    # Check number of cities
    if len(cities) != 22:
        return "FAIL"

    for idx, tour in enumerate(tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # Check that each tour starts and ends at the depot

        previous_city_index = tour[0]
        for city_index in tour[1:]:
            if city_index != 0:  # don't add demand for depot
                total_demand_met[city_index] += demands[city_index]
                total_capacity_used[idx] += demands[city_index]
                all_visits.add(city_index)

            # Calculate travel cost
            dist = euclidean_distance(cities[previous_city_index], cities[city_index])
            individual_costs[idx] += dist
            previous_city_index = city_index

        if abs(individual_costs[idx] - costs[idx]) > 0.01:
            return "FAIL"  # Check calculated cost consistency

        if total_capacity_used[idx] > robot_capacity:
            return "FAIL"  # Check robot capacity

    # Check if every city (except depot) is visited and demands met exactly
    for city_index in range(1, len(demands)):
        if total_demand_met[city_index] != demands[city_index]:
            return "FAIL"

    # Check if overall cost is calculated correctly
    if abs(sum(costs) - sum(individual_costs)) > 0.01:
        return "FAIL"

    # If all tests are passed
    return "CORRECT"

# Definitions based on the solution provided and the cities and their demands
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
robot_capacity = 6000

tours = [
    [0, 1, 2, 3, 4, 6, 7, 8, 9, 0],
    [0, 5, 10, 11, 12, 14, 0],
    [0, 13, 15, 16, 17, 21, 0],
    [0, 18, 19, 20, 0]
]

costs = [193.18, 129.78, 136.09, 122.23]

result = verify_solution(tours, costs, demands, robot_capacity, cities)
print(result)