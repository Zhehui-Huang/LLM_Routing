import math
from itertools import permutations

# Setting up the city data
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [
    0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15
]
num_robots = 2
robot_capacity = 160

# Calculate the Euclidean distance between two cities
def distance(index1, index2):
    x1, y1 = coordinates[index1]
    x2, y2 = coordinates[index2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate feasible tours that respect robot capacity constraints
def get_feasible_tours():
    feasible_tours = []
    cities = list(range(1, len(coordinates)))  # exclude the depot
    for perm in permutations(cities):
        tour = [0] + list(perm) + [0]  # start and end at the depot
        if is_tour_feasible(tour):
            feasible_tours.append(tour)
    return feasible_tours
    
def is_tour_feasible(tour):
    current_load = 0
    for city in tour[1:-1]:  # skip the depot entry and exit in tour path
        current_load += demands[city]
        if current_load > robot_capacity:
            return False
    return True

# Calculate the travel cost of a tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Assign optimal routes to robots and calculate minimum cost
def optimal_robot_assignment(feasible_tours):
    optimal_cost = float('inf')
    optimal_assignment = None
    for assignment in permutations(feasible_tours, num_robots):
        if covers_all_cities(assignment):
            cost = sum(tour_cost(tour) for tour in assignment)
            if cost < optimal_cost:
                optimal_cost = cost
                optimal_assignment = assignment
    return optimal_assignment, optimal_cost

def covers_all_cities(assignment):
    covered = set()
    for tour in assignment:
        covered.update(tour[1:-1])  # skip depot
    return len(covered) == len(coordinates) - 1  # match total cities minus depot

# Finding suitable tours and the optimal assignment
feasible_tours = get_feasible_tours()
assignment, total_cost = optimal_robot_assignment(feasible_tours)

# Display results
if assignment:
    for idx, tour in enumerate(assignment):
        print(f"Robot {idx} Tour: {tour}")
        print(f"Robot {idx} Total Travel Cost: {tour_cost(tour)}")
    print(f"Overall Total Travel Cost: {total_cost}")
else:
    print("No feasible solution found.")