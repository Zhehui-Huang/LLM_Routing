import math
from sys import maxsize

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def initialize_robot_tours(num_robots, cities, depot_coord):
    robot_tours = [[] for _ in range(num_robots)]
    for i, city in enumerate(cities):
        # Assign cities to robots in a round-robin manner
        robot_tours[i % num_robots].append(city)
    return robot_tours

def create_initial_tours(robot_tours, depot_coord):
    tours = []
    for tour in robot_tours:
        path = [0]  # start at depot
        current_position = depot_coord
        # Find nearest neighbor tour
        while tour:
            closest_distance = maxsize
            closest_city_index = None
            for i in range(len(tour)):
                dist = euclidean_distance(current_position, tour[i])
                if dist < closest_distance:
                    closest_distance = dist
                    closest_city_index = i
            current_position = tour.pop(closest_city_index)
            path.append(current_position)
        path.append(0)  # return to depot
        tours.append(path)
    return tours

def two_opt(tour, distance_calculator):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: 
                    continue # These are consecutive edges
                if distance_calculator(tour[i-1], tour[i]) + distance_calculator(tour[j], tour[j+1]) > distance_calculator(tour[i-1], tour[j]) + distance_calculator(tour[i], tour[j+1]):
                    tour[i:j+1] = reversed(tour[i:j+1])
                    improved = True
    return tour

def calculate_tour_cost(tour, distance_calculator):
    cost = 0
    for i in range(len(tour)-1):
        cost += distance_calculator(tour[i], tour[i+1])
    return cost

def solve_mtsp(cities, num_robots):
    depot_coord = cities.pop(0)
    robot_tours = initialize_robot_tours(num_robots, cities, depot_coord)
    initial_tours = [[depot_coord] + tour + [depot_coord] for tour in robot_tours]
    improved_tours = []

    for tour in initial_tours:
        improved_tour = two_opt(tour, lambda x, y: euclidean_distance(x, y))
        improved_tours.append(improved_tour)

    total_cost = 0
    for i, tour in enumerate(improved_tours):
        cost = calculate_tour_cost(tour, lambda x, y: euclidean_city_distance(x, y))
        total_cost += cost
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {cost}")
    
    print(f"Overall Total Travel Cost: {total_cost}")

# City coordinates
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]

# Number of robots
num_robots = 8

solve_mtsp(cities, num_robots)