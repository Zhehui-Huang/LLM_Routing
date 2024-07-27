import math
from itertools import permutations

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
    (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Number of robots
num_robots = 2

# Find all partitions of the cities into two subsequences
def find_partitions(cities, k):
    def directed_partition(i):
        if i == len(cities):
            yield tuple(partition)
            return
        for idx in range(len(partition)):
            if len(partition[idx]) < k:
                partition[idx].append(cities[i])
                yield from directed_partition(i + 1)
                partition[idx].pop()
            if len(partition[idx]) == 0:
                break

    cities = list(cities)
    partition = [[] for _ in range(k)]
    yield from directed_partition(0)

# Calculate the total travel cost of a tour starting and ending at the depot
def tour_cost(tour):
    cost = 0
    current_city = 0  # Start at the depot
    for city in tour:
        cost += euclidean_distance(current_city, city)
        current_city = city
    cost += euclidean_distance(current_city, 0)  # Return to depot
    return cost

# Generate all routes and calculate costs to find the minimum maximum cost for any robot
all_cities = list(range(1, 21))  # All cities excluding the depot
min_max_cost = float('inf')
best_distribution = None

for partition in find_partitions(all_cities, num_robots):
    tours = []
    costs = []
    feasible = True
    for subroute in partition:
        if len(subroute) > 0:
            total_cost = tour_cost(subroute)
            costs.append(total_cost)
            tours.append([0] + subroute + [0])
    if costs:
        max_cost = max(costs)
        if max_cost < min_max_cost:
            min_max_cost = max_cost
            best_distribution = (tours, costs)

if best_distribution:
    tours, costs = best_distribution
    for i, tour in enumerate(tours):
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {costs[i]}")
    print(f"Maximum Travel Cost: {min_max_cost}")
else:
    print("No feasible solution found.")