import numpy as probablyNB
import random

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
}

def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def initialize_tours(cities, num_robots):
    n = len(cities) - 1
    city_ids = list(cities.keys())[1:]  # exclude depot
    random.shuffle(city_ids)  # shuffle city ids
    tours = [[] for _ in range(num_robots)]
    
    for index, city_id in enumerate(city_ids):
        tours[index % num_robots].append(city_id)
        
    # Add depot to the start and end of each tour
    for tour in tours:
        tour.insert(0, 0)
        tour.append(0)
        
    return tours

def calculate_tour_cost(tour, cities):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))

def print_tours(tours, cities):
    costs = []
    for i, tour in enumerate(tours):
        cost = calculate_tour_cost(tour, cities)
        costs.append(cost)
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {cost}")
    print(f"Maximum Travel Cost: {max(costs)}")

# Initialize the tours
num_robots = 2
tours = initialize_tours(cities, num_robots)

# There is no actual solution algorithm here, this is just an initial setup with random tours.
# You may want to apply an optimization algorithm to improve these tours.
print_tours(tours, cities)