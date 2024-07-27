import numpy as np
import math

# Coordinates for all cities including depots
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Euclidean distance calculation function
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Number of robots and starting city for all is depot at city 0
num_robots = 8
start_city = 0

# This example uses a simplistic round-robin distribution for cities to each robot
visited = {city: False for city in cities}
tours = [[] for _ in range(num_robots)]
visited[start_city] = True  # Mark the depot as visited
current_cities = [start_city] * num_robots

while not all(visited.values()):
    for i in range(num_robots):
        min_distance = float('inf')
        next_city = None
        for city in cities:
            if not visited[city]:
                distance = euclidean_map((current_cities[i], city))
                if distance < min_distance:
                    min_distance = distance
                    next_city = city
        if next_city is not None:
            tours[i].append(next_city)
            current_cities[i] = next_city
            visited[next_city] = True

# Adding start depot to complete each tour
for tour in tours:
    tour.insert(0, start_city)

# Calculate costs for each tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i + 1])
    return total_cost

# Display results
overall_total_travel_cost = 0
for i, tour in enumerate(tours):
    tour_cost = calculate_tour_cost(tour)
    overall_total_travel_cost += tour_cost
    print(f"Robot {i} Tour: [{', '.join(map(str, tour))}]")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")
print(f"Overall Total Travel Cost: {overall_total_travel_cost:.2f}")