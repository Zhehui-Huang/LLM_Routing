import math
import random

# Cities and their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208), 
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189), 
    20: (155, 185), 21: (139, 182)
}

# Number of robots and their corresponding depot city
num_robots = 4
depots = [0, 1, 2, 3]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Initial solution generation, one simple way: cyclic distribution of cities
def initial_solution(depots, cities):
    non_depots = [city for city in cities if city not in depots]
    random.shuffle(non_depots)
    chunks = [non_depots[i::num_robots] for i in range(num_robots)]
    tours = [[depots[i]] + chunks[i] for i in range(num_robots)]
    return tours

# Calculate total cost of tours
def calculate_total_cost(tours):
    total_cost = 0
    for tour in tours:
        cost = 0
        for i in range(len(tour) - 1):
            cost += euclidean_distance(tour[i], tour[i + 1])
        cost += euclidean_distance(tour[-1], tour[0])  # Close the tour
        tour.append(cost)
        total_cost += cost
    return total_cost

# Simulated annealing procedure
def simulated_annealing(tours, initial_temp=1000, cooling_rate=0.99, num_iterations=1000):
    T = initial_temp
    best_tours = tours
    best_cost = calculate_total_cost(tours)
    
    for _ in range(num_iterations):
        for tour in best_tours:
            # Create a new candidate tour by swapping two cities in the tour
            i, j = random.sample(range(1, len(tour)-1), 2)  # Skip the first city because it's depot
            tour[i], tour[j] = tour[j], tour[i]
            new_cost = calculate_total_cost(best_tours)
            if new_cost < best_cost or random.random() < math.exp(-(new_cost - best_cost) / T):
                best_cost = new_remaining_miles
            else:
                # Swap back if not accepted
                tour[i], tour[j] = tour[j], tour[i]
        T *= cooling_rate

    return best_tours

# Initialize and run the SA algorithm
initial_tours = initial_solution(depots, cities)
optimized_tours = simulated_annealing(initial_tours)

# Output results
overall_cost = 0
for i, tour in enumerate(optimized_tours):
    cost = tour.pop()  # Remove cost from list, previously appended in calculate_total_cost
    overall_cost += cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")