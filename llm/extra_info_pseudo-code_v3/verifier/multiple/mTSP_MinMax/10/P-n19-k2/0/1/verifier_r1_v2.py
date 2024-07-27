import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution(robot_tours, city_coordinates, robot_costs, maximum_reported_cost):
    all_cities = set(range(len(city_coordinates)))  # Set of all city indices
    visited_cities = set()  # Set to track cities that have been visited

    total_travel_costs = []  # List to store travel costs for each robot's tour

    for tour in robot_tours:
        # Ensure the tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Check if each city in the tour is visited only once and collect all visited cities
        for i in range(1, len(tour) - 1):
            city = tour[i]
            if city in visited_cities:
                return "FAIL"
            visited_cities.add(city)

        # Calculating the travel cost for the current tour
        travel_cost = sum(calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]]) for i in range(len(tour) - 1))
        total_travel_costs.append(travel_cost)

    # Check if all non-depot cities are visited and only they are visited
    if visited_cities != (all_cities - {0}):
        return "FAIL"

    # Compare reported costs against calculated costs
    for reported_cost, calculated_cost in zip(robot_costs, total_travel_costs):
        if not math.isclose(reported_cost, calculated_cost, rel_tol=1e-5):
            return "FAIL"

    # Check the maximum reported travel cost
    if not math.isclose(max(total_travel_costs), maximum_reported_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# City coordinates
cities_coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]

# Provided tours for each robot
robot_tours = [[0, 1, 3, 4, 8, 10, 11, 12, 14, 16, 17, 0], [0, 2, 5, 6, 7, 9, 13, 15, 18, 0]]

# Reported costs for each robot's tour
robot_costs = [212.21732723337922, 116.70009709276687]

# Reported maximum travel cost
maximum_reported_cost = 212.21732723337922

# Call the check function
result = check_solution(robot_tours, cities_coordinates, robot_costs, maximum_reported_cost)
print(result)