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

# Robot tours
robot_tours = [
    [0, 19, 16, 4, 0],
    [0, 5, 20, 12, 7, 0],
    [0, 13, 11, 1, 17, 15, 9, 0],
    [0, 18, 3, 21, 2, 10, 6, 14, 8, 0]
]

robot_capacity = 6000

def verify_solution(robot_tours, cities_coordinates, demands, robot_capacity):
    all_demands_met = True
    capacity_constraints_met = True
    start_end_depot = True
    total_travel_cost = 0

    demand_covered = [0] * len(demands)

    for tour in robot_tours:
        load = 0
        if tour[0] != 0 or tour[-1] != 0:
            start_end_depot = False

        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i + 1]
            travel_cost = calculate_distance(cities_coordinates[city_from], cities_coordinates[city_to])
            total_travel_cost += travel_cost
            load += demands[city_to]
            demand_covered[city_to] += demands[city_to]
        
        if load > robot_capacity:
            capacity_constraints_met = False

    for city_idx in range(1, len(demands)):
        if demand_covered[city_idx] != demands[city_idx]:
            all_demands_met = False
    
    conditions_met = start_end_depot and all_demands_met and capacity_constraints——met
    return conditions_met, total_travel_cost

correct, calculated_cost = verify_solution(robot_tours, cities_coordinates, cities_demand, robot_capacity)
print("CORRECT" if correct else "FAIL")
print(f"Calculated Total Travel Cost: {calculated_cost}")