import math

# City coordinates (index represents city ID)
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of robots
num_robots = 2

def compute_distance(city1, city2):
    """Calculate Euclidean distance between two cities given their coordinates."""
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

def two_opt(tour):
    """Optimize the tour using the 2-opt algorithm."""
    optimized = True
    while optimized:
        optimized = False
        for i in range(len(tour) - 1):
            for j in range(i+2, len(tour)):
                if j-i == 1:
                    continue
                if compute_distance(tour[i], tour[i+1]) + compute_distance(tour[j], tour[j+1]) > compute_distance(tour[i], tour[j]) + compute_distance(tour[i+1], tour[j+1]):
                    tour[i+1:j+1] = reversed(tour[i+1:j+1])
                    optimized = True
    return tour

def initialize_tours():
    """Assign cities to robots using round-robin assignment."""
    tours = [[] for _ in range(num_robots)]
    for city in range(1, len(coordinates)):  # Starting from 1 to skip the depot
        tours[city % num_robots].append(city)
    return tours

def calculate_tour_cost(tour):
    """Calculates the total cost of a tour."""
    cost = 0
    for i in range(len(tour) - 1):
        cost += compute_distance(tour[i], tour[i+1])
    return cost

# Initial assignment of cities
tours = initialize_tours()

final_tours = []
final_costs = []

for index, tour in enumerate(tours):
    # Include the depot at the start and end of the tour
    tour = [0] + tour + [0]
    optimized_tour = two_opt(tour)
    cost = calculate_tour_cost(optimized_tour)
    
    final_tours.append(optimized_tour)
    final_costs.append(cost)

    print(f"Robot {index} Tour: {optimized_tour}")
    print(f"Robot {index} Total Travel Cost: {cost}")

# Print total cost across all robots
print(f"Overall Total Travel Cost: {sum(final_costs)}")