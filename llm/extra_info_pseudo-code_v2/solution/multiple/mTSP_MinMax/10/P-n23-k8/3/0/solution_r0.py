import math
from random import shuffle, randint, random

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots
num_robots = 8

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Initialize tours for each robot
def initialization():
    sorted_cities = sorted(list(cities.keys())[1:], key=lambda x: distance(0, x))
    tours = {i: [0] for i in range(num_robots)}
    
    # Distribute cities to robots
    for i, city in enumerate(sorted_cities):
        tours[i % num_robots].append(city)
        
    for i in range(num_robots):
        tours[i].append(0)
    
    return tours

# Calculate cost of each tour
def compute_tour_cost(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Perform Shaking (Randomization)
def shake(tours):
    r1, r2 = randint(0, num_robots - 1), randint(0, num_robots - 1)
    if len(tours[r1]) > 2 and len(tours[r2]) > 2:
        i1, i2 = randint(1, len(tours[r1]) - 2), randint(1, len(tours[r2]) - 2)
        tours[r1][i1], tours[r2][i2] = tours[r2][i2], tours[r1][i1]
    return tours

# Main algorithm implementation
def gvns(tmax=100):
    current_tours = initialization()
    best_tours = current_tours
    best_maximum_cost = max(compute_tour_cost(tour) for tour in best_tours.values())
    
    time = 0
    while time < tmax:
        current_tours = shake(current_tours)
        max_cost = max(compute_tour_cost(tour) for tour in current_tours.values())
        
        if max_cost < best_maximum_cost:
            best_tours = current_tours
            best_maximum_cost = max_cost
        
        time += 1
    
    return best_tours, best_maximum_cost

# Running the algorithm
tours, max_travel_cost = gvns()

# Output the results
for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {compute_tour_cost(tours[i])}")
print(f"Maximum Travel Cost: {max_travel_cost}")