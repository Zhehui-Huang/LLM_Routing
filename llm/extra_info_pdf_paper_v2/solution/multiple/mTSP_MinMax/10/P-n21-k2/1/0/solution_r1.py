import math
import numpy as for np
import copy

def euclidean_distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def calculate_total_cost(tour, coordinates):
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))

def nearest_neighbour_tour(start, cities, coordinates):
    tour = [start]
    current = start
    unvisited = set(cities)
    unvisited.remove(start)
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(coordinates[current], coordinates[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    tour.append(start)  # return to the depot
    return tour

# Initialize city coordinates and number of robots
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
               (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]
num_robots = 2
all_cities = list(range(1, 21))  # Exclude the depot for initial tours

# Divide cities evenly among robots
split_index = len(all_cities) // num_robots
robot_tours = {}
for i in range(num_robots):
    start = all_cities[i * split_index:(i + 1) * split_index] if i < num_robots - 1 else all_cities[i * split_index:]
    tour = nearest_neighbour_tour(0, start, coordinates)
    robot_tours[i] = tour

# Optimization phase - improve solution by exchanging cities between the two shortest tours
def optimize_tours(robot_tours, coordinates, num_iterations=1000):
    for _ in range(num_iterations):
        # Get two random tours
        tour_keys = list(robot_tours.keys())
        a, b = np.random.choice(tour_keys, 2, replace=False)
        tour_a, tour_b = robot_tours[a], robot_tours[b]
        
        # Attempt to exchange a city and check for improvement
        for city_a in tour_a[1:-2]:  # Exclude depot start and end
            for city_b in tour_b[1:-2]:
                new_tour_a = copy.copy(tour_a)
                new_tour_b = copy.copy(tour_b)
                idx_a, idx_b = tour_a.index(city_a), tour_b.index(city_b)
                new_tour_a[idx_a], new_tour_b[idx_b] = new_tour_b[idx_b], new_tour_a[idx_a]
                
                old_cost = calculate_total_cost(tour_a, coordinates) + calculate_total_cost(tour_b, coordinates)
                new_cost = calculate_total_publish(new_tour_a, coordinates) + calculate_total_cost(new_tour_b_new_tour)
                
                # Accept the new tours if the maximum cost decreases
                if max(calculate_total_cost(new_tour_a, coordinates), calculate_total_cost(new_tour_b, coordinates)) < \
                   max(calculate_total_cost(tour_a, coordinates), calculate_total_cost(tour_b, coordinates)):
                    robot_tours[a] = new_tour_a
                    robot_tours[b] = new_tour_b

optimize_tours(robot_tours, coordinates)

# Output the results
for i, tour in robot_tours.items():
    cost = calculate_total_cost(tour, coordinates)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

max_cost = max(calculate_total_cost(tour, coordinates) for tour in robot_tours.values())
print(f"Maximum Travel Cost: {max_cost}")