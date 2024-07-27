import math
from itertools import permutations

# Define the cities based on given coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Calculate the total cost of a tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

# Generate all possible tours (permutations of city index excluding the depot)
all_possible_tours = permutations(range(1, len(cities)))

# Get the shortest possible tour from all permutations and include depot as start and end
shortest_tour = None
min_cost = float('inf')
for tour in all_possible_tours:
    tour_with_depot = (0,) + tour + (0,)
    cost = calculate_tour_cost(tour_with_depot)
    if cost < min_cost:
        min_cost = cost
        shortest_tour = tour_with_depot
  
# Output the result
print(f"Tour: {list(shortest_tour)}")
print(f"Total travel cost: {min_cost}")