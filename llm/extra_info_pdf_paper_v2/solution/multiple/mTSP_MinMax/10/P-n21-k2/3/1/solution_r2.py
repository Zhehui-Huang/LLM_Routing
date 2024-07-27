import math
import random
from copy import deepcopy

# City coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Initialize random tours
def initialize_tours(num_robots, cities):
    n = len(cities)
    city_indices = list(range(1, n))
    random.shuffle(city_indices)
    # Split cities approximately evenly
    tours = [[] for _ in range(num_robots)]
    for i, city in enumerate(city_indices):
        tours[i % num_robots].append(city)
    # Wrap tours to start and end at the depot
    for tour in tours:
        tour.insert(0, 0)
        tour.append(0)
    return tours

# Calculate the cost of a tour
def calculate_tour_cost(tour):
    return sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Function to make a deep copy of tours and try interchanging cities between two tours to see if there's improvement
def optimize_tours(tours):
    best_tours = deepcopy(tours)
    min_max_cost = max(calculate_tour_cost(tour) for tour in tours)
    improvement = True
    
    while improvement:
        improvement = False
        for i in range(len(tours)):
            for j in range(len(tours)):
                if i != j:
                    for idx1 in range(1, len(tours[i])-1):
                        for idx2 in range(1, len(tours[j])-1):
                            # Swap and calculate new max cost
                            tours[i][idx1], tours[j][idx2] = tours[j][idx2], tours[i][idx1]
                            new_max_cost = max(calculate_tour_cost(tour) for tour in tours)
                            if new_max_cost < min_max_cost:
                                min_max_cost = new_max_cost
                                best_tours = deepcopy(tours)
                                improvement = True
                            else:
                                # Swap back if no improvement
                                tours[i][idx1], tours[j][idx2] = tours[j][idx2], tours[i][idx1]
    return best_tours

# Initialize random tours for robots
random.seed(0)  # For reproducibility
initial_tours = initialize_tours(2, cities)
optimized_tours = optimize_tours(initial_tours)

# Calculate the cost of each tour
tour_costs = [calculate_tour_cost(tour) for tour in optimized_tours]
max_tour_cost = max(tour_costs)

# Print results
print("Optimized Tours and Costs:")
for i, (tour, cost) in enumerate(zip(optimized_tours, tour_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")
print(f"Maximum Travel Cost: {max_tour_cost:.2f}")