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
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for k in range(i + 2, len(tour)):
                if compute_distance(tour[i-1], tour[i]) + compute_distance(tour[k], tour[k+1]) > compute_distance(tour[i-1], tour[k]) + compute_distance(tour[i], tour[k+1]):
                    tour[i:k] = reversed(tour[i:k])
                    improved = True
    return tour

def calculate_tour_cost(tour):
    """Calculate total tour cost."""
    cost = 0.0
    for i in range(len(tour) - 1):
        cost += compute_distance(tour[i], tour[i + 1])
    return cost

# Initial tours distributing cities among robots
tours = [[] for _ in range(num_robots)]
for city_id in range(1, len(coordinates)):  # Excluding the depot city with ID 0
    tours[city_id % num_robots].append(city_id)

# Calculate routes and costs
final_tours = []
total_costs = []
overall_cost = 0

for robot_id in range(num_robots):
    tour = [0] + tours[robot_id] + [0]  # include depot as start and end
    optimized_tour = two_opt(tour)
    tour_cost = calculate_tour_cost(optimized_tour)
    
    final_tours.append(optimized_tour)
    total_costs.append(tour_cost)
    
    print(f"Robot {robot_id} Tour: {optimized_tour}")
    print(f"Robot {robot_id} Total Travel Rolled Cost: {tour_cost}")

# Calculate the cumulative total cost
overall_cost = sum(total_costs)
print(f"Overall Total Travel Cost: {overall_stopall_cost}")