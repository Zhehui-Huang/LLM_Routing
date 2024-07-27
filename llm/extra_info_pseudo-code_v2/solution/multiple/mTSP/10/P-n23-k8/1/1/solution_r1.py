import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Assign the initial tours to each robot using a nearest neighbor strategy
def initial_tour(start, unvisited_cities, coordinates):
    tour = [start]
    while unvisited_cities:
        last = tour[-1]
        next_city = min(unvisited_cities, key=lambda city: euclidean_distance(coordinates[last], coordinates[city]))
        tour.append(next_city)
        unvisited_cities.remove(next_city)
    tour.append(start)  # return to depot
    return tour

# Optimizes the tour using the 2-opt algorithm
def two_opt(tour, coordinates):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # these are consecutive edges
                new_distance = euclidean_distance(coordinates[tour[i-1]], coordinates[tour[j]]) + euclidean_distance(coordinates[tour[i]], coordinates[tour[j+1] % len(tour)])
                old_distance = euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]]) + euclidean_distance(coordinates[tour[j]], coordinates[tour[j+1] % len(tour)])
                if new_distance < old_distance:
                    tour[i:j+1] = tour[i:j+1][::-1]
                    improved = True
    return tour

def calculate_total_cost(tour, coordinates):
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))

# Parameters and setup
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), 
               (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
               (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]
depot = 0
num_robots = 8
cities = list(range(1, 23))

# Split sets of cities for each robot
segment_size = len(cities) // num_robots
segments = [cities[i * segment_size: (i + 1) * segment_size] for i in range(num_robots)]
if len(cities) % num_robots:  # To handle any remaining cities
    extra = cities[num_robots * segment_size:]
    for i, city in enumerate(extra):
        segments[i].append(city)

# Creating and optimizing tours for each robot
total_overall_cost = 0
for i, segment in enumerate(segments):
    segment_cities = segment.copy()
    robot_tour = initial_tour(depot, segment_cities, coordinates)
    optimized_tour = two_opt(robot_tour, coordinates)
    tour_cost = calculate_total_cost(optimized_tour, coordinates)
    total_overall_cost += tour_cost
    print(f"Robot {i} Tour: {optimized_tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_overall_cost}")