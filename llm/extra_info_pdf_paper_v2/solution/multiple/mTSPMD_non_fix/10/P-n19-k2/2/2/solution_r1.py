import math
import random

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Initial crude solution
def create_initial_solution():
    # Start from the depots
    tours = [[0], [1]]
    unvisited = list(cities.keys())[2:]  # cities except depots
    random.shuffle(unvisited)
    # Arbitrarily divide unvisited cities between the two robots
    tours[0].extend(unopened[:len(unvisited)//2])
    tours[1].extend(unvisited[len(unvisited)//2:])
    return tours

# Calculate cost of a tour
def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Simulated Annealing to optimize each tour
def simulated_annealing(tour):
    temp = 10000  # initial temperature
    cooling_rate = 0.003
    while temp > 1:
        # Create new tour as a neighbor
        new_tour = tour[:]
        i, j = sorted(random.sample(range(1, len(tour)), 2))
        new_tour[i:j] = reversed(new_tour[i:j])  # reverse subsequence
        
        # Decide if we should accept the neighbor
        old_cost = calculate_tour_cost(tour)
        new_cost = calculate_tour_cost(new_tour)
        if new_cost < old_cost or math.exp((old_cost - new_cost) / temp) > random.random():
            tour = new_tour
        
        temp *= (1 - cooling_rate)
    
    return tour

# Generate and optimize initial solution
initial_tours = create_initial_solution()
optimized_tours = [simulated_annealing(tour) for tour in initial_tours]

# Calculate costs
costs = [calculate_tour_cost(tour) for tour in optimized_tours]
total_cost = sum(costs)

# Output results
for i, tour in enumerate(optimized_tours):
    print(f"Robot {i} Tour: {tour + [tour[0]]}")  # tour ending at its starting depot
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Overall Total Travel Cost: {total_cost}")