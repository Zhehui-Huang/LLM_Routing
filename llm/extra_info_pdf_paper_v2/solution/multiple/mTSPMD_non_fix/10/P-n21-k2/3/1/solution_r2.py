import math
import random

# City Coordinates (index corresponds to city number, where 0 and 1 are depots)
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(city1, city2):
    # Calculate Euclidean distance between two cities
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0])**2 + (city_coords[city1][1] - city_coords[city2][1])**2)

def calculate_total_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def initial_solution():
    cities = list(range(2, 21))  # all cities excluding depots
    random.shuffle(cities)
    # Split randomly into two approximately equal subsets
    midpoint = len(cities) // 2
    robot0_tour = [0] + cities[:midpoint]  # robot 0 starts and ends at depot 0
    robot1_tour = [1] + cities[midpoint:]  # robot 1 starts and ends at depot 1
    return [robot0_tour, robot1_tour]

def optimize_tour(tour):
    # A very simple optimization: repeatedly try swapping two cities and accept if it improves the tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                # Swap two cities
                new_tour = tour[:i] + [tour[j]] + tour[i+1:j] + [tour[i]] + tour[j+1:]
                if calculate_total_tour_cost(new_tour) < calculate_total_tour_cost(tour):
                    tour = new_tour
                    improved = True
    return tour

# Generate initial solution and optimize it
tours = initial_solution()
tours = [optimize_tour(tour + [tour[0]]) for tour in tours]  # Append depot to end and optimize

# Calculate costs
costs = [calculate_total_tour_cost(tour) for tour in tours]
total_cost = sum(costs)

# Output results
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Overall Total Travel Cost: {total_cost}")