import math
import itertools

# Define cities coordinate
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58), 6: (12, 84),
    7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94),
    14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Calculate all pairs distances
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(i, j)

# Solve the TSP variant
def select_and_solve_tsp(cities, num_cities=13):
    min_tour = []
    min_cost = float('inf')
    
    for chosen_cities in itertools.combinations(cities.keys() - {0}, num_cities - 1):
        total_cities = [0] + list(chosen_cities)
        
        # Finding a near-optimal tour among these cities + depot
        current_cost, current_tour = greedy_tsp(total_cities)
        
        if current_cost < min_cost:
            min_cost = current_cost
            min_tour = current_tour
            
    return min_tour, min_cost

# Greedy algorithm to find a tour given selected cities
def greedy_tsp(cities):
    unvisited = set(cities)
    tour = [0]  # start at the depot
    unvisited.remove(0)
    cost = 0
    
    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda x: distances[(last, x)])
        cost += distances[(last, next_recipe)]
        tour.append(next_city)
        unvisited.remove(next_city)
    
    # Return to depot
    cost += distances[(tour[-1], 0)]
    tour.append(0)
    
    return cost, tour

# Main execution to find the best tour out of the given cities
optimal_tour, optimal_cost = select_and_solve_tsp(cities)

print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost}")