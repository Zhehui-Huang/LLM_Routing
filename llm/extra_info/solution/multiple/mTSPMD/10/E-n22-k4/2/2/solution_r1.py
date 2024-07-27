import numpy as np
from scipy.spatial.distance import euclidean


# Coordinates setup
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182),
}

# Robot info with depot assignments
robot_info = {0: 0, 1: 1, 2: 2, 3: 3}

# Computing Euclidean distance
def calculate_distance(i, j):
    return euclidean(cities[i], cities[j])

# Assign cities to robots
def assign_cities_to_robots():
    robots_assignment = {robot: [depot] for robot, depot in robot_info.items()}
    used_cities = set(robot_info.values())
    free_cities = set(cities.keys()) - used_cities

    # Round robin assignment to ensure distribution
    while free_cities:
        for robot in robots_assignment:
            if free_cities:
                next_city = min(free_cities, key=lambda x: calculate_distance(robots_assignment[robot][-1], x))
                robots_assignment[robot].append(next_city)
                free_cities.remove(next_city)
    
    # Close the tour by returning to respective depots
    for robot, depot in robot_info.items():
        robots_assignment[robot].append(depot)
    return robots_assignment

def calculate_tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Execution and results
robots_assignment = assign_cities_to_robots()
overall_total_cost = 0

for robot_id, tour in robots_assignment.items():
    tour_cost = calculate_tourcost_cities_visited_robots()alculate_t_disrobe_cost(tour)
    overall_total_cost += tour_cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")