import math
from itertools import permutations

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_tour_cost(tour, coordinates):
    """Calculate the total travel cost for a given tour."""
    cost = 0
    for i in range(1, len(tour)):
        cost += calculate_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    return cost

def find_min_max_distance_partition(cities, coordinates, num_robots):
    """Find a partition of cities that minimizes the maximum travel distance by any robot."""
    best_max_distance = float('inf')
    best_tours = None
    # Iterate over all the ways to partition the cities into `num_robots` groups
    for partition in permutations(cities, len(cities)):
        # Split the permutation into `num_robots` parts approximately evenly
        tours = []
        for i in range(num_robots):
            start = i * len(cities) // num_robots
            end = (i + 1) * len(cities) // num_robots
            tour = [0] + list(partition[start:end]) + [0]
            tours.append(tour)
        
        # Calculate the cost of each tour and find the maximum distance any robot needs to travel
        max_distance = max(calculate_tour_cost(tour, coordinates) for tour in tours)
        
        # Update the best tours found if the current max distance is less than the previously found
        if max_distance < best_max_distance:
            best_max_distance = max_distance
            best_tours = tours
        
    return best_tours, best_max_distance

coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
    (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]
cities = list(range(1, 21))  # city indices excluding the depot, which is index 0
num_robots = 2

best_tours, best_max_distance = find_min_max_distance_partition(cities, coordinates, num_robots)

# Outputting the best tours and the overall maximum distance
for i, tour in enumerate(best_tours):
    tour_cost = calculate_tour_cost(tour, coordinates)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

print(f"Maximum Travel Cost: {best_max_distance:.2f}")