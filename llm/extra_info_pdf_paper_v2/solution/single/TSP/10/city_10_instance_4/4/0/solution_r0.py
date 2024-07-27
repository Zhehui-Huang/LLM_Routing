import math
import random

# Define the city coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Compute the total travel cost of a tour
def total_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Function to generate a random tour starting and ending at the depot (city 0)
def random_tour():
    tour = list(cities.keys())
    middle = tour[1:]  # exclude the depot city for shuffling
    random.shuffle(middle)
    return [0] + middle + [0]

# Function to try to improve the tour by swapping two cities and checking if it improves the cost
def try_to_improve(tour):
    best_cost = total_cost(tour)
    best_tour = tour[:]
    improved = False

    for i in range(1, len(tour) - 2):
        for j in range(i + 1, len(tour) - 1):
            new_tour = tour[:]
            new_tour[i:j+1] = reversed(new_tour[i:j+1])
            new_cost = total_cost(new_tour)
            if new_cost < best_cost:
                best_cost = new_cost
                best_tour = new_tour[:]
                improved = True
    return improved, best_tour

# Lin-Kernighan heuristic-like approach
def lin_kernighan_heuristic():
    best_tour = random_tour()
    best_cost = total_cost(best_tour)
    
    improving = True
    while improving:
        improving, new_tour = try_to_improve(best_tour)
        if improving:
            best_tour = new_tour
            best_cost = total_cost(best_tour)
    
    return best_tour, best_cost

# Running the algorithm to find the best tour
best_tour, min_cost = lin_kernighan_heuristic()

# Displaying the results as specified
print("Tour:", best_tour)
print("Total travel cost:", min_cost)