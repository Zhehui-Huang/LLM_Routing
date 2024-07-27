import math
import random

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Initial greedy selection of cities excluding the depot
def greedy_select_cities(depot, num_cities, total_cities):
    remaining_cities = list(range(1, total_cities))
    tour = [depot]
    current = depot

    while len(tour) < num_cities:
        next_city = min(remaining_cities, key=lambda x: euclidean_distance(current, x))
        tour.append(next_city)
        remaining_cities.remove(next_city)
        current = next_city

    return tour

# Simulated annealing to improve the initial tour
def simulated_annealing(tour, temperature=1000, cooling_rate=0.98, steps=1000):
    def swap_cities(current_tour):
        new_tour = current_tour[:]
        idx1, idx2 = random.sample(range(1, len(new_tour) - 1), 2)
        new_tour[idx1], new_tour[idx2] = new_tour[idx2], new_tour[idx1]
        return new_tour
    
    current_cost = calculate_tour_cost(tour)
    best_tour = tour[:]
    best_cost = current_cost
    
    for step in range(steps):
        temp_tour = swap_cities(tour)
        temp_cost = calculate_tour_cost(temp_tour)
        if temp_cost < current_cost or random.random() < math.exp((current_cost - temp_cost) / temperature):
            tour = temp_tour
            current_cost = temp_cost
            if temp_cost < best_cost:
                best_tour = temp_tour
                best_cost = temp_cost
        temperature *= cooling_rate
    
    return best_tour, best_cost

# Calculate total cost of the tour
def calculate_tour_cost(tour):
    total_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    return total_cost

# Main execution to find solution
initial_tour = greedy_select_cities(0, 7, len(cities))
initial_tour.append(0)  # Return to the depot
optimized_tour, total_cost = simulated_annealing(initial_tour)

# Output the results
print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {total_cost:.2f}")