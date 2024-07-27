import random
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_travel_cost(tour, coordinates):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return cost

def generate_initial_tour(depot, cities, k):
    selected_cities = random.sample(cities, k - 1)
    selected_cities.insert(0, depot)
    selected_cities.append(depot)
    return selected_cities

def local_search(tour, coordinates):
    best_tour = tour[:]
    min_cost = total_travel_cost(tour, coordinates)
    
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = total_travel_cost(new_tour, coordinates)
                if new_cost < min_cost:
                    best_tour = new_tour[:]
                    min_cost = new_cost
                    improved = True
    return best_tour, min_cost

def k_tsp_gvns(coordinates, k):
    depot = 0
    cities = list(range(1, len(coordinates)))
    
    best_tour = generate_initial_tour(depot, cities, k)
    best_cost = total_travel_cost(best_tour, coordinates)
    
    iterations = 0
    while iterations < 1000:
        current_tour = generate_initial_tour(depot, cities, k)
        current_tour, current_cost = local_search(current_tour, coordinates)

        if current_cost < best_cost:
            best_tour = current_tour[:]
            best_cost = current_cost

        iterations += 1
    
    return best_tour, best_cost

# Coordinates of the cities
coordinates = [
    (16, 90),  # Depot city 0
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

# Find the optimal tour visiting exactly 10 cities
best_tour, best_cost = k_tsp_gvns(coordinates, 10)
print("Tour:", best_tour)
print("Total travel cost:", best_cost)