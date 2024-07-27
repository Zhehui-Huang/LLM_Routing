import random
import math

# Define cities and their coordinates
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

# Function to calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Function to generate a random initial tour of exactly 7 cities including the depot
def generate_initial_tour():
    tour = random.sample(list(cities.keys())[1:], 6)  # Picking 6 other cities randomly
    tour.insert(0, 0)  # Adding depot city at the start
    tour.append(0)  # Adding depot city at the end to complete the tour
    return tour

# Function to compute the total tour cost
def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Function to shake the tour by swapping two non-depot cities
def shake(tour):
    tour = tour[1:-1]  # Remove depot from both ends to avoid swapping it
    idx1, idx2 = random.sample(range(len(tour)), 2)  # Pick two indices to swap
    tour[idx1], tour[idx2] = tour[idx2], tour[idx1]
    return [0] + tour + [0]  # Reinsert the depot back to both ends

# Variable Neighborhood Descent function
def vnd(tour):
    current_cost = calculate_tour_cost(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):  # Skip the depot
            for j in range(i + 1, len(tour) - 1):
                if i == 0 or j == len(tour) - 1:
                    continue  # Skip if trying to swap the depot city
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = calculate_tour_cost(new_tour)
                if new_cost < current_cost:
                    tour, current_cost = new_tour, new_cost
                    improved = True
    return tour

# GVNS function
def gvns(num_restarts):
    best_tour = generate_initial_tour()
    best_cost = calculate_tour_cost(best_tour)
    
    for _ in range(num_restarts):
        current_tour = generate_initial_tour()
        current_cost = calculate_tour_cost(current_tour)
        
        for _ in range(100):  # Number of iterations for local search and shaking
            shaken_tour = shake(current_tour)
            locally_optimal_tour = vnd(shaken_tour)
            local_cost = calculate_tour_cost(locally_optimal_tour)
            
            if local_cost < current_cost:
                current_tour, current_cost = locally_optimal_tour, local_cost  # Accept the new solution
            
            if current_cost < best_cost:
                best_tour, best_cost = current_tour, current_cost  # Update best found solution
    
    return best_tour, best_cost

# Run the GVNS
best_tour, best_cost = gvns(10)

# Output the best tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))