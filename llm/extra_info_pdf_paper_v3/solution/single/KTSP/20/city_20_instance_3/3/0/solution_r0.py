import math
import random

# Define the cities' coordinates
cities = [
    (30, 56),  # Depot city 0
    (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77),
    (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

def euclidean_distance(a, b):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def total_tour_cost(tour):
    """Calculate the total cost of a given tour."""
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

def simulated_annealing(tour):
    """Optimize tour using a simulated annealing algorithm."""
    temp = 1000
    min_temp = 1
    alpha = 0.99
    current_tour = tour[:]
    current_cost = total_tour_cost(current_tour)
    best_tour = current_tour[:]
    best_cost = current_cost
    
    while temp > min_temp:
        for _ in range(100):
            i = random.randint(1, len(tour) - 3)
            j = random.randint(i + 1, len(tour) - 2)
            new_tour = current_tour[:]
            new_tour[i:j+1] = reversed(new_tour[i:j+1])
            new_cost = total_tour_cost(new_tour)
            if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
                current_tour, current_cost = new_tour[:], new_cost
                if current_cost < best_cost:
                    best_tour, best_cost = current_tour[:], current_cost
                    
        temp *= alpha
    
    return best_tour, best_cost

def greedy_subset_selection():
    """Select a subset of cities using a nearest neighbor heuristic."""
    selected = [0]
    candidates = set(range(1, 20))
    
    while len(selected) < 13:
        last = selected[-1]
        next_city = min(candidates, key=lambda x: euclidean_distance(cities[last], cities[x]))
        selected.append(next_city)
        candidates.remove(next_city)
    
    selected.append(0)  # Returning to the depot
    return selected

# Select cities greedily
initial_tour = greedy_subset_selection()

# Optimize the initial tour through simulated annealing
final_tour, final_cost = simulated_annealing(initial_tour)

print(f"Tour: {final_tour}")
print(f"Total travel cost: {final_cost}")