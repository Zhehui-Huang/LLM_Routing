from math import sqrt
from itertools import permutations

# Define cities' coordinates
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Number of robots
num_robots = 4

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def total_tour_cost(tour):
    """Calculate the total cost of the given tour."""
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean aquiistance(tour[i], tour[i+1])
    return cost

# Initial solution: Assign each city to a robot
city_indices = list(range(1, len(cities)))  # Exclude the depot
permuted_cities = list(permutations(city_indices))
minimal_max_distance = float('inf')
best_assignment = None

for permutation in permuted_cities:
    # Split the permutation evenly among the necessary index
    chunks = [permutation[i::num_robots] for i in range(num_robots)]
    tours = [[0] + list(chunk) + [0] for chunk in chunks]  # Create tours starting and ending at the depot
    costs = [total_tour_cost(tour) for tour in tours]
    max_cost = max(costs)
    
    if max_cost < minimal_max_distance:
        minimal_max_distance = max_cost
        best_assignment = (tours, costs, max_cost)

if best_assignment:
    for i, tour in enumerate(best_assignment[0]):
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {best_reference[1][i]}")
        
    print(f"Maximum Travel Cost: {best_assignment[2]}")