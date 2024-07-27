import math
import random

# Define the cities with their coordinates
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), 
          (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), 
          (83, 96), (60, 50), (98, 1)]

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Evaluate the total distance of a tour
def evaluate_tour(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate an initial random tour
def generate_initial_solution():
    tour = [0]
    while len(tour) < 6:
        new_city = random.choice([i for i in range(1, 15) if i not in tour])
        tour.append(new_city)
    tour.append(0)
    return tour

# Neighborhood shaking: Swap two random cities 
def shake(tour):
    i, j = random.sample(range(1, 5), 2)  # choose two indices to swap (exclude depot)
    tour[i], tour[j] = tour[j], tour[i]
    return tour

# Local search using two neighborhood structures
def local_search(tour):
    best_tour = tour[:]
    best_cost = evaluate_tour(tour)
    
    # N1: Exchange operation
    for i in range(1, 5):  # Exclude depot
        for j in range(1, 15):  # Try exchanging with other cities
            if j not in tour:
                new_tour = tour[:]
                new_tour[i] = j
                new_tour[-1] = 0  # Ensure return to depot
                cost = evaluate_tour(new_tour)
                if cost < best_cost:
                    best_tour = new_tour
                    best_cost = cost
    
    return best_tour

# GVNS algorithm
def GVNS():
    best_tour = generate_initial_solution()
    best_cost = evaluate_tour(best_tour)
    for iter in range(100):
        current_tour = shake(best_tour[:])
        current_tour = local_search(current_tour)
        current_cost = evaluate_tour(current_tour)
        if current_cost < best_cost:
            best_tour = current_tour
            best_cost = current_cost
    return best_tour, best_cost

# Run the algorithm
tour, cost = GVNS()
print(f"Tour: {tour}")
print(f"Total travel cost: {cost:.2f}")