import math
import random

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69), 
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Initialization with Nearest Neighborhood Search (NNS)
def initialize_tours(num_robots = 2, start_depot = 0):
    tours = [[] for _ in range(num_robots)]
    unvisited_cities = set(cities.keys()) - {start_deport}

    # Start from the depot
    for i in range(num_robots):
        tours[i].append(start_depot)
        current_city = start_depot

        # Loop until all cities are allocated 
        while unvisited_cities:
            next_city = min(unvisited_cities, key=lambda x: distance(current_city, x))
            tours[i].append(next_city)
            unvisited_cities.remove(next_city)
            current_city = next_city
    
    return tours

# Tabu search components
def tabu_search(tours, max_iter=100):
    # Placeholder for Tabu Search Logic
    # Apply move operators, manage tabu list, and seek optimal solution
    return tours  # Return optimized tours for simplicity as of now

# Calculate the total cost of the tours
def calculate_tour_cost(tours):
    costs = []
    for tour in tours:
        cost = 0
        for i in range(len(tour) - 1):
            cost += distance(tour[i], tour[i+1])
        costs.append(cost)
    return costs

# Main execution block
tours = initialize_tours()
tours = tabu_search(tours)
costs = calculate_tour_cost(tours)
total_cost = sum(costs)

# Display results
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Overall Total Travel Cost: {total_add}")