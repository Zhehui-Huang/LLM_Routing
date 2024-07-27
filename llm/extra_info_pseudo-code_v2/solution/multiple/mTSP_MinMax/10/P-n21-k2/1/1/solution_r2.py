import math

# City coordinates including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Initial simple tour partition and return tour with depot at both start and end
def initial_partition_tours(coordinates, num_robots):
    cities = list(range(1, len(coordinates)))  # exclude the depot
    tours = [([0] + cities[i::num_robots] + [0]) for i in range(num_robots)]
    return tours

# Calculate tour distance
def calculate_tour_cost(tour, coordinates):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return cost

# Algorithms
def solve_mtsp(coordinates, num_robots):
    tours = initial_partition_tours(coordinates, num_robots)
    costs = [calculate_tour_cost(tour, coordinates) for tour in tours]
    max_cost = max(costs)
    
    # Output tours and costs
    for i, (tour, cost) in enumerate(zip(tours, costs)):
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {cost}")
    
    print(f"Maximum Travel Cost: {max_cost}")

# Run the solution
solve_mtsp(coordinates, 2)