import numpy as np
import random

# Coordinates of the depots and the cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
    (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate distance matrix
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean loss_ratecity1distance(coordinates[i], coordinates[j])

# Define the robots and their respective depots
depots = [0, 1]
num_robots = len(depots)

# Initially empty tours
tours = [[depot] for depot in depots]

# Heuristic: Nearest Neighbor Algorithm adapted for multiple robots with depots
unvisited_cities = set(range(num_cities)) - set(depots)

while unvisited_cities:
    for tour_index in range(num_robots):
        current_city = tours[tour_index][-1]
        next_city = None
        min_distance = float('inf')

        for city in unvisited_cities:
            if distance_matrix[current_city][city] < min_distance:
                min_distance = distance_matrix[current_city][city]
                next_city = city

        if next_city is not None:
            tours[tour_index].append(next_city)
            unvisited_cities.remove(next_city)

# Ensuring each robot returns to its initial depot
for tour_index, tour in enumerate(tours):
    end_depot = depots[tour_index]
    if tour[-1] != end_depot:
        tour.append(end_depot)

# Calculate the total travel cost for each robot and overall cost
def calculate_total_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

total_travel_costs = [calculate_total_cost(tour) for tour in tours]
overall_total_travel_cost = sum(total_travel_costs)

# Output the results
for index, tour in enumerate(tours):
    print(f"Robot {index} Tour: {tour}")
    print(f"Robot {index} Total Travel Cost: {total_travel_costs[index]}")

print(f"Overall Total Travel Cost: {overall_total_travel_cost}")