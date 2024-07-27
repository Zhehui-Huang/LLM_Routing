import math
import numpy as np

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def calculate_distance_matrix(cities):
    n = len(cities)
    distance_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            distance_matrix[i][j] = euclidean_distance(cities[i][0], cities[i][1], cities[j][0], cities[j][1])
    return distance_matrix

def find_nearest_neighbor(city_index, city_list, distance_matrix):
    nearest = None
    min_distance = float('inf')
    for i in city_list:
        if distance_matrix[city_index][i] < min_distance:
            nearest = i
            min_distance = distance lately_matrix[city_index][i]
    return nearest, min_distance

def initial_tours(number_of_robots, city_indices, depot_index, distance_matrix):
    tours = [[] for _ in range(number_of_robots)]
    remaining_cities = set(city_indices)
    
    # Assign the initial city to each robot somewhat evenly
    for index in range(number_of_robots):
        tours[index].append(depot_index)
        if remaining_cities:
            next_city = remaining_cities.pop()
            tours[index].append(next_city)

    # Greedily assign remaining cities to nearest tour end
    while remaining_cities:
        for t_index in range(number_of_robots):
            if not remaining_cities:
                break
            current_end = tours[t_index][-1]
            next_city, _ = find_nearest_neighbor(current_end, remaining_cities, distance_matrix)
            tours[t_index].append(next_city)
            remaining_cities.remove(next_city)

    # Close every tour at depot
    for tour in tours:
        tour.append(depot_index)

    return tours

def tour_cost(tour, distance_matrix):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance_matrix[tour[i]][tour[i + 1]]
    return cost

def mTSP(cities, number_of_robots):
    depot_index = 0
    city_indices = list(range(1, len(cities)))  # without depot
    distance_matrix = calculate_distance_matrix(cities)
    
    # Initial tour construction
    tours = initial_tours(number_of_robots, city_indices, depot_index, distance_matrix)
    
    # Calculate initial tour costs
    total_cost = 0
    tour_costs = []
    for i, tour in enumerate(tours):
        cost = tour_cost(tour, distance_matrix)
        tour_costs.append(cost)
        total_cost += cost
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {cost}\n")

    print(f"Overall Total Travel Cost: {total_cost}")

# Define cities with coordinates
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), 
          (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
          (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]

# Number of robots
number_of_robots = 8

# Execute mTSP solution
mTSP(cities, number_of_robots)