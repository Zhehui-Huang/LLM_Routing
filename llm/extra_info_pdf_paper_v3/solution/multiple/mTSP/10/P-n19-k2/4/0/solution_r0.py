import math
from itertools import permutations

# City coordinates
coordinates = [
    (30, 40),  # Depot city 0
    (37, 52),
    (49, 43),
    (52, 64),
    (31, 62),
    (52, 33),
    (42, 41),
    (52, 41),
    (57, 58),
    (62, 42),
    (42, 57),
    (27, 68),
    (43, 67),
    (58, 27),
    (37, 69),
    (61, 33),
    (62, 63),
    (63, 69),
    (45, 35)
]

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities given their coordinates"""
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Number of robots
num_robots = 2

# Compute all possible tours for a single robot
def all_possible_tours(cities):
    tours = permutations(cities)
    return [[0] + list(tour) + [0] for tour in tours]

# Calculate the total travel cost of a tour
def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Divide cities among robots
def assign_cities_to_robots(num_robots, cities):
    # This is a simple partitioning, a more complex one could yield better results
    n = len(cities)
    k, m = divmod(n, num_robots)
    return [cities[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(num_robot)]

# Initial partition
city_sets = assign_cities_to_robots(num_robots, list(range(1, len(coordinates))))

# Calculate all tours for all robots
all_tours = [all_possible_tours(city_set) for city_set in city_sets]

# Finding the shortest tours for each robot
shortest_tours = []
for tours in all_tours:
    min_tour = min(tours, key=calculate_tour_cost)
    shortest_tours.append(min_tour)

# Calculate travel costs for the shortest tours
tour_costs = [calculate_tour_cost(tour) for tour in shortest_tours]
overall_total_cost = sum(tour_costs)

# Output results
for i, tour in enumerate(shortest_tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")

print(f"Overall Total Travel Cost: {overall_total_cost}")