import numpy as np
from math import sqrt
from heapq import heappop, heappush
import random
import time

# Define the cities coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35),
    21: (32, 39),
    22: (56, 37)
}

num_robots = 8

def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Function to calculate the total distance of the tour
def calculate_tour_distance(tour, city_coordinates):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    return total_distance

def initialization(num_robots, cities):
    # Start each robot at the depot
    tours = {i: [0] for i in range(num_robots)}
    remaining_cities = list(cities.keys())[1:]  # exclude the depot city

    # Assign each city to the nearest available robot tour
    while remaining_cities:
        for tour_idx in tours:
            if remaining_cities:
                next_city = min(remaining_cities, key=lambda x: euclidean_distance(cities[0], cities[x]))
                tours[tour_idx].append(next_city)
                remaining_cities.remove(next_city)
            else:
                break

    # Return each robot to the depot
    for tour_idx in tours:
        tours[tour_idx].append(0)

    return tours

def shake(tours, k):
    # Shaking process: randomly relocate k cities in the tours
    flat_tours = [(tour_idx, city) for tour_idx, tour in tours.items() for city in tour[1:-1]]
    random.shuffle(flat_tours)
    
    for _ in range(k):
        if len(flat_tours) > 1:
            (tour_idx1, city1), (tour_idx2, city2) = random.sample(flat_tours, 2)
            # Swap cities
            tours[tour_idx1].remove(city1)
            tours[tour_idx2].remove(city2)
            tours[tour_idx1].insert(1, city2)  # insert after the depot
            tours[tour_idx2].insert(1, city1)  # insert after the depot

    return tours

def seq_vnd(tours, city_coordinates):
    improved = True
    while improved:
        improved = False
        for tour_idx, tour in tours.items():
            best_distance = calculate_tour_distance(tour, city_coordinates)
            # Try all 2-opt moves
            n = len(tour)
            for i in range(1, n - 2):
                for j in range(i + 1, n - 1):
                    if j - i == 1: continue  # these are adjacent already
                    new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                    new_distance = calculate_tour_distance(new_tour, city_coordinates)
                    if new_distance < best_distance:
                        tours[tour_idx] = new_tour
                        best_distance = new_distance
                        improved = True
    return tours

def gvns(city_coordinates, num_robots, lmax, kmax, tmax):
    # Initialization
    tours = initialization(num_robots, city_coordinates)
    start_time = time.time()
    
    while time.time() - start_time < tmax:
        k = 1
        while k < kmax:
            new_tours = shake(dict(tours), k)
            new_tours = seq_vnd(new_tours, city_coordinates)
            new_max_distance = max(calculate_tour_distance(tour, city_coordinates) for tour in new_tours.values())
            curr_max_distance = max(calculate_tour_distance(tour, city_coordinates) for tour in tours.values())
            if new_max_distance < curr_max_distance:
                tours = new_tours
                k = 1  # Reset k since improvement was made
            else:
                k += 1

    return tours

# GVNS parameters
lmax = 5  # limit for VND
kmax = 10  # max level for shaking
tmax = 60  # maximum running time in seconds

# Run GVNS
final_tours = gvns(cities, num_robots, lmax, kmax, tmax)

# Calculate costs and find maximum travel cost
costs = []
for idx, tour in final_tours.items():
    cost = calculate_tour_distance(tour, cities)
    costs.append(cost)
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

max_cost = max(costs)
print(f"Maximum Travel Cost: {max_cost}")