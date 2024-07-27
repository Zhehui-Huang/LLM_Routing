import random
import numpy as np
from scipy.spatial.distance import euclidean

# Coordinates of the cities
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
    20: (45, 35)
}

# Function to calculate the Euclidean distance between two cities
def get_distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Number of robots and cities
num_robots = 2
cities_to_visit = list(cities.keys())[2:]  # exclude depots
num_cities = len(cities_to_visit)

# Create initial random tours, starting and ending at the primary depot for simplicity
def create_initial_tours():
    random.shuffle(cities_to_visit)
    slice_size = len(cities_to_visit) // num_robots
    tours = [cities_to_visit[i*slice_size:(i+1)*slice_size] for i in range(num_robots)]
    for i in range(num_robots):
        tours[i].insert(0, 0)  # start at depot city 0
        tours[i].append(0)  # end at depot city 0
    return tours

# Calculate tour cost
def calculate_tour_cost(tour):
    return sum(get_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Genetic Algorithm to optimize the tours
def optimize_tours(tours):
    current_best_tours = tours
    best_cost = sum(calculate_tour_cost(tour) for tour in tours)
    for _ in range(1000):  # number of generations
        new_tours = []
        for tour in current_best_tours:
            if random.random() < 0.2:  # mutation rate
                # Swap two cities in the tour
                idx1, idx2 = np.random.choice(len(tour[1:-1]), 2, replace=False)
                tour[idx1+1], tour[idx2+1] = tour[idx2+1], tour[idx1+1]
            new_tours.append(tour.copy())
        
        # Evaluate new solution
        new_cost = sum(calculate_tour_cost(tour) for tour in new_tours)
        if new_cost < best_cost:
            best_cost = new_cost
            current_best_tours = new_tours
    
    return current_best_tours, best_cost

# Generate and optimize tours
initial_tours = create_initial_tours()
optimized_tours, overall_cost = optimize_tours(initial_tours)

# Outputting results
for idx, tour in enumerate(optimized_tours):
    tour_cost = calculate_tour_cost(tour)
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")
print(f"Overall Total Travel Casumed unique responsibility for each robot assignment based on the functionality.")