import math

# Define city coordinates (index corresponds to city number)
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), 
    (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69), 
    (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35)
]

# Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Visits all cities using a nearest neighbor heuristic from a starting city and returns the tour and cost
def nearest_neighbor_tour(start_city, cities):
    tour = [start_city]
    unvisited = set(range(len(cities)))
    unvisited.remove(start_city)
    current_city = start_city
    total_cost = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance(cities[current_city], cities[x]))
        total_cost += distance(cities[current_city], cities[next_city])
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)
    
    total_cost += distance(cities[current_city], cities[start_city])
    tour.append(start_city)
    return tour, total_cost

# Splits the cities into approximately equal parts and assigns them to multiple robots
def split_cities_for_robots(num_robots, cities):
    step = len(cities[1:]) // num_robots
    return [cities[0:1] + cities[1:][i*step:(i+1)*step] for i in range(num_robots)]

# Assign initial routes for 2 robots
num_robots = 2
split_cities = split_cities_for_robots(num_robots, cities)
robot_tours = []
total_travel_cost = 0

for i in range(num_robots):
    tour, cost = nearest_neighbor_tour(0, split_cities[i])
    robot_tours.append((tour, cost))
    total_travel_cost += cost
    
# Print result
for index, (tour, cost) in enumerate(robot_tours):
    print(f"Robot {index} Tour: {tour}")
    print(f"Robot {index} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_travel_cost}")