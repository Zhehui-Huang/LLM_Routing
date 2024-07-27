import math
import itertools

def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Generate initial greedy tours for each robot
def initialize_tours(num_robots):
    remaining_cities = set(cities.keys()) - {0}
    tours = {i: [0] for i in range(num_robots)}
    
    while remaining_cities:
        for i in range(num_robots):
            if not remaining_cities:
                break
            # Find the nearest city to the last city in the tour
            last_city = tours[i][-1]
            next_city = min(remaining_cities, key=lambda c: euclidean_distance(last_city, c))
            tours[i].append(next_city)
            remaining_cities.remove(next_city)
    
    # Add the depot to the end of each tour
    for i in range(num_robots):
        tours[i].append(0)
    
    return tours

# Calculate total travel cost for a given tour
def calculate_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Assign tours to robots and compute costs
def solve_mtsp(num_robots):
    tours = initialize_tours(num_robots)
    total_costs = []
    
    # Compute cost for each tour
    for i in range(num_robots):
        cost = calculate_cost(tours[i])
        total_costs.append(cost)
        print(f"Robot {i} Tour: {tours[i]}")
        print(f"Robot {i} Total Travel Cost: {cost:.2f}\n")
    
    # Compute and print the overall total cost
    overall_total_cost = sum(total_costs)
    print(f"Overall Total Travel Cost: {overall_total to {s}s_cost:.2f}")

solve_mtsp(2)