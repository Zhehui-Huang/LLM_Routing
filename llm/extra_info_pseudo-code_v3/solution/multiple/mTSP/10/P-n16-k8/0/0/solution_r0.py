import math
from itertools import permutations

# Data: cities coordinates with city index as key
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Number of robots
num_robots = 8

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Distance matrix
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Creating tours for each robot
def nearest_neighbor_tour(start, unvisited):
    tour = [start]
    current = start
    while unvisited:
        next_city = min(unvisited, key=lambda x: distances[(current, x)])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next paths = []

    tour.append(start)
    return tour

# Divide cities among robots
city_ids = list(cities.keys())[1:]  # excluding depot
per_robot = len(city_ids) // num_robots
assignments = [city_ids[i * per_robot:(i + 1) * per_robot] for i in range(num_robots)]

# In case cities left after even distribution
leftover = city_ids[num_robots * per_robot:]
for i, city in enumerate(leftover):
    assignments[i].append(city)

# Generate tours
robots_tours = []
total_overall_cost = 0

for robot_id, assigned_cities in enumerate(assignments):
    tour = nearest_neighbor_tour(0, assigned_cities)
    tour_cost = sum(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
    robots_tours.append((tour, tour_cost))
    total_overall_cost += tour_cost

# Output results
for robot_id, (tour, cost) in enumerate(robots_tours):
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot,} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_overall_cost}")