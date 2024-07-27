import math
import itertools

# Define cities coordinates (index corresponds to city number)
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
    15: (37, 69)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Heuristic: Greedy partitions based on proximity to depot extended to fair partitioning
def greedy_partition(cities, k):
    # Depot is the first city
    depot = 0
    remaining_cities = list(cities.keys())[1:]
    clusters = {i: [] for i in range(k)}
    remaining_cities = sorted(remaining_cities, key=lambda x: distance(depot, x))
    
    # Simple round-robin assignment to ensure roughly equal distribution
    for index, city in enumerate(remaining_cities):
        clusters[index % k].append(city)
    
    return clusters

# Solve TSP for a single robot using a simple nearest neighbor algorithm
def tsp_tour(start_city, cities):
    unvisited = cities.copy()
    tour = [start_city]
    current_city = start_city

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current_city, city))
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)
    
    tour.append(start_city)  # return to depot
    return tour

# Compute total cost of a tour
def compute_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Main simulation
def simulate_robots_and_tours():
    num_robots = 8
    clusters = greedy_partition(cities, num_robots)
    tours = []
    costs = []

    for i in range(num_robots):
        if clusters[i]:
            tour = tsp_tour(0, clusters[i])
            tours.append(tour)
            costs.append(compute_cost(tour))
        else:
            tours.append([0, 0])  # empty tour for robots with no cities
            costs.append(0)

    max_cost = max(costs) if costs else 0
    
    # Displaying the results:
    for index, tour in enumerate(tours):
        if len(tour) > 1:  # Only if the robot has a tour
            print(f"Robot {index} Tour: {tour}")
            print(f"Robot {index} Total Travel Cost: {costs[index]}")

    print(f"Maximum Travel Cost: {max_cost}")

simulate_robots_and_tours()