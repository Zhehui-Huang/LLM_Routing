import math
import random

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
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate the distance matrix
distances = [[euclidean_distance(cities[i], cities[j]) for j in cities] for i in cities]

# Assign cities to robots using a simple nearest neighbor cluster initialization
def assign_cities_to_robots(cities, num_robots, depot=0):
    # Exclude depot and use city indices
    city_indices = list(cities.keys())
    city_indices.remove(depot)

    # Randomly distribute cities to each robot initially
    random.shuffle(city_indices)
    assignments = [city_indices[i::num_robots] for i in range(num_robots)]
    return assignments

assigned_cities = assign_cities_to_robots(cities, num_robots)

# Construct initial tours using nearest neighbor heuristic
def nearest_neighbor_tour(start_city, cities):
    tour = [0, start_city]
    unvisited = set(cities)
    unvisited.remove(start_city)
    while unvisited:
        last_city = tour[-1]
        next_city = min(unvisited, key=lambda city: distances[last_city][city])
        unvisited.remove(next_city)
        tour.append(next_city)
    tour.append(0)  # return to the depot
    return tour

# Generate tours for each robot
tours = []
for i in range(num_robots):
    if assigned_cities[i]:
        start_city = assigned_cities[i][0]
        tour = nearest_neighbor_tour(start_city, assigned_cities[i])
        tours.append(tour)
    else:
        tours.append([0, 0])  # if no cities were assigned, stay at the depot

# Calculate the cost of the tours
def calculate_tour_cost(tour):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Display the results
total_travel_cost = 0
for i, tour in enumerate(tours):
    cost = calculate_tour_cost(tour)
    total_travel_cost += cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {round(cost, 2)}")

print(f"Overall Total Travel Cost: {round(total_travel_cost, 2)}")