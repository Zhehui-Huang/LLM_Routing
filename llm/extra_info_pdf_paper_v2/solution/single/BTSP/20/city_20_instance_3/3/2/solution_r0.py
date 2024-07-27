import math
import itertools

# City coordinates indexed from 0 to 19, where index 0 is the depot city.
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), 
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

def euclidean_dist(a, b):
    """ Calculate the Euclidean distance between two cities. """
    return math.hypot(cities[a][0] - cities[b][0], cities[a][1] - cities[b][1])

### Step 2: Implement Heuristic Approach
# Using a greedy algorithm to build an initial solution.
def greedy_bottleneck_tour(start_city):
    unvisited = set(range(1, len(cities)))
    tour = [start_city]
    current_city = start_city
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_dist(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
        
    tour.append(start_city)  # returning to the depot
    return tour

### Step 3: Calculate the Metrics
def tour_metrics(tour):
    total_distance = sum(euclidean_dist(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    max_distance = max(euclidean_dist(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    return total_distance, max_distance

### Execution of Solution
# Generate a tour starting from the depot city (0)
tour = greedy_bottleneck_tour(0)
total_distance, max_distance = tour_metrics(tour)

### Output
print("Tour:", tour)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", max_distance)