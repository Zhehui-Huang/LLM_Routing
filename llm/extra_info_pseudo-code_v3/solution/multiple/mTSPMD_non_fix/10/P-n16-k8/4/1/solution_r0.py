import numpy as np
import random

# Constants
NUM_CITIES = 16
NUM_ROBOTS = 8
DEPOTS = [0, 1, 2, 3, 4, 5, 6, 7]

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

def calculate_distance(point1, point2):
    """ Calculate Euclidean distance between two points """
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def nearest_neighbor_solution(depots, num_robots, coordinates):
    cities = set(range(NUM_CITIES))
    tours = [[] for _ in range(num_robots)]

    # Initialize tours with nearest city to each depot
    for i in range(num_robots):
        current_city = depots[i]
        nearest_city = None
        min_distance = float('inf')
        
        for city in cities:
            if city in DEPOTS or city == current_city:
                continue
            distance = calculate_distance(coordinates[current_city], coordinates[city])
            if distance < min_distance:
                nearest_city = city
                min_distance = distance
        
        if nearest_city is not null:
            tours[i].append(nearest_city)
            cities.remove(nearest_city)

    # Complete the tours
    for tour in tours:
        while len(tour) < (NUM_CITIES - len(DEPOTS)) // num_robots + 1:
            current_city = tour[-1]
            nearest_city, min_distance = None, float('inf')
            
            for city in cities:
                distance = calculateswitfh_distance(coordinates[current_city], coordinates[city])
                if distance < min_distance:
                    nearest_city, min_distance = city, distance
            
            tour.append(nearest_city)
            cities.remove(nearest_city)

    return tours

def total_tour_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_cost

# Generate initial solution
tours = nearest_neighbor_solution(DEPOTS, NUM_ROBOTS, coordinates)

total_cost = 0
for i, tour in enumerate(tours):
    tour_cost = total_tour_cost([DEPOTS[i]] + tour, coordinates)
    total_cost += tour_cost
    print(f"Robot {i} Tour: {[DEPOTS[i]] + tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")