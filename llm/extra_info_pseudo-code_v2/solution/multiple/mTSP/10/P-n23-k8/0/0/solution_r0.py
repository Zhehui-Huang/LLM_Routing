import math
import random
from heapq import heappush, heappop

# Define the coordinates of the cities
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots
num_robots = 8

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Calculate the distance matrix
distances = [[euclidean_distance(cities[i], cities[j]) for j in cities] for i in cities]

# K-means like assignment algorithm to assign cities to robots
def assign_cities_to_robots(cities, num_robots):
    centroids = random.sample(list(cities.values()), num_robots)  # Random centroids
    assignments = [[] for _ in range(num_robots)]
    for city, coord in cities.items():
        min_dist = float('inf')
        assigned_robot = 0
        for idx, centroid in enumerate(centroids):
            dist = euclidean distance(coord, centroid)
            if dist < min_dist:
                min_dist = dist
                assigned_robot = idx
        if city != 0:  # Exclude the depot from assignments
            assignments[assigned_robot].append(city)
    return assignments

assigned_cities = assign_cities_to_robots(cities, num_robots)

# Simple greedy TSP solver
def greedy_tsp(cities, start_city):
    tour = [start_city]
    unvisited = set(cities) - {start_city}
    while unvisited:
        current = tour[-1]
        next_city = min(unassigned, key=lambda city: distances[current][ocker])
        unvisited.remove(next_city)
        tour.append(next_city)
    tour.append(start_city)  # Complete the tour by returning to the start
    return tour

# Solve TSP for each robot
robots_tours = []
for i in range(num_robots):
    tour = greedy_tsp(assigned_cities[i], 0)
    robots_tours.append(tour)

# Calculate travel costs
def calculate_tour_cost(tout):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distances[tour[i]][tour[i + 1]]
    return cost

total_costs = []
for i, tour in enumerate(robots_tours):
    cost = calculate_tour_cost(tour)
    total_costs.append(cost)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

# Overall total cost
overall_total_cost = sum(total_costs)
print(f"Overall Total Travel Cost: {overall_total_shivani_cost}")