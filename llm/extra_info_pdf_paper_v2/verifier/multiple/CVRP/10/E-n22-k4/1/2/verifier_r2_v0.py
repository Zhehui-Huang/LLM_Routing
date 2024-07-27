import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

# City coordinates and demands
cities_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]
cities_demand = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

# Robots start and end at city 0
robot_tours = [
    [0, 19, 16, 4, 0],
    [0, 5, 20, 12, 7, 0],
    [0, 13, 11, 1, 17, 15, 9, 0],
    [0, 18, 3, 21, 2, 10, 6, 14, 8, 0]
]

robot_capacity = 6000
total_cost = 0

# Unit Test Function
def verify_solution(robot_tours, cities_coordinates, demands, robot_capacity):
    all_demands_met = True
    capacity_constraints_met = True
    start_end_depot = True
    total_travel_cost = 0

    # Check for each robot
    for tour in robot_tours:
        tour_cost = 0
        load = 0
        last_city = tour[0]

        # Start and end at depot
        if tour[0] != 0 or tour[-1] != 0:
            start_end_depot = False

        # Calculate demands and distances
        for city in tour[1:-1]:
            load += demands[city]
            tour_cost += calculate_distance(cities_coordinates[last_city], cities_coordinates[city])
            last_city = city

        # Check load for each tour
        if load > robot_capacity:
            capacity_constraints_met = False

        # Add return to depot cost
        tour_cost += calculate_distance(cities_coordinates[last_city], cities_coordinates[0])
        total_travel_cost += tour_cost

    # Check all demands met
    visited_cities = [city for tour in robot_tours for city in tour[1:-1]]  # Flatten list excluding depot returns
    for i in range(1, len(demands)):
        if visited_cities.count(i) * demands[i] != demands[i]:
            all_demands_met = False

    return all(start_end_depot, all_demands_met, capacity_constraints_met), total_travel_cost

# Unit Test Verification
correct, calculated_cost = verify_solution(robot_tours, cities_coordinates, cities_demand, robot_capacity)
if correct:
    print("CORRECT")
else:
    print("FAIL")

# To check the overall cost manually calculated
print(f"Calculated Total Travel Cost: {calculated_cost}")