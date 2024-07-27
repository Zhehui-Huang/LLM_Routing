import numpy as np
import random

# Define the cities and their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 
    14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193), 
    18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
}

# Distance calculation (Euclidean)
def distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Heuristic: Nearest Neighbor Search
def nearest_neighbor(depot, unvisited):
    current = depot
    tour = [depot]
    tour_length = 0
    while unvisited:
        nearest = min(unvisited, key=lambda x: distance(current, x))
        tour_length += distance(current, nearest)
        tour.append(nearest)
        current = nearest
        unvisited.remove(nearest)
    return tour, tour_length

# Assign cities to robots: Very basic initial split (not near optimal)
robots = 4
depots = [0] * robots  # Robots start at depot 0
cities_per_robot = len(cities) // robots
tours = []
total_cost = 0

assigned_cities = list(cities.keys())[4:]  # Assuming first 4 keys are depots; adjust logic for different setups
random.shuffle(assigned_cities)  # Randomize city order to mimic random distribution

# Assign and calculate tours for each robot
for i in range(robots):
    if i < robots - 1:
        cities_subset = assigned_cities[i*cities_per_robot:(i+1)*cities_per_robot]
    else:
        cities_subset = assigned_cities[i*cities_per_robot:]  # Last robot gets the remainder
    
    cities_subset = [0] + cities_subset  # start at depot 0
    tour, cost = nearest_neighbor(0, cities_subset[1:])
    tour.append(0)  # Make the end at the starting depot for simplicity
    cost += distance(tour[-2], tour[-1])  # Close the loop back to depot
    
    tours.append(tour)
    total_cost += cost

    # Output the tour for each robot
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

# Output the overall total cost
print(f"\nOverall Total Travel Cost: {total_cost:.2f}")