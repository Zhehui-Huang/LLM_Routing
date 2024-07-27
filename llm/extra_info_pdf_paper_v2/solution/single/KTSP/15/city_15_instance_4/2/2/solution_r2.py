import random
import math

# Define the locations of the cities
cities = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
          (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
          (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)]

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# k-TSP using a random start heuristic followed by variable neighborhood search
def variable_neighborhood_search(k, max_iter=1000):
    best_tour = random.sample(range(1, len(cities)), k-1)  # random k-1 cities (excluding depot city)
    best_tour = [0] + best_tour + [0]  # start and end at the depot city
    
    # Calculate the total travel cost of the tour
    def tour_cost(tour):
        return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

    best_cost = tour_cost(best_tour)

    # Simple local search by swapping within tour
    def local_search(tour):
        n = len(tour)
        best_local_tour = tour.copy()
        best_local_cost = tour_cost(tour)
        for i in range(1, n-1):
            for j in range(i+1, n-1):
                new_tour = tour.copy()
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = tour_cost(new_tour)
                if new_cost < best_local_cost:
                    best_local_cost = new_cost
                    best_local_tour = new_tour
        return best_local_tour
    
    # Improvement by variable neighborhood search
    iteration = 0
    while iteration < max_iter:
        new_tour = local_search(best_tour)
        new_cost = tour_cost(new_tour)
        if new_cost < best_cost:
            best_tour = new_tour
            best_cost = new_cost
        else:
            break
        iteration += 1
    
    return best_tour, best_cost

# Solve using the defined GVNS algorithm
k = 12  # including the depot city
best_solution_tour, best_solution_cost = variable_neighborhood_search(k)

# Output the tour and the cost
print("Tour:", best_solution_tour)
print("Total travel cost:", round(best_solution_cost, 2))