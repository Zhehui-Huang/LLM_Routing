import random
import math

# Coordinates for each city
cities = [
    (50, 42),  # Depot city (0)
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

def generate_initial_solution():
    selected_cities = [0]  # Start at the depot
    available_cities = list(range(1, len(cities)))  # Exclude the depot from available cities
    random.shuffle(available_cities)
    selected_cities.extend(available_cities[:3])
    selected_cities.append(0)  # Return to depot
    return selected_cities

def local_search(tour):
    best_tour = tour[:]
    best_cost = calculate_tour_cost(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour)-2):
            for j in range(i+1, len(tour)-1):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # Swap two cities
                new_cost = calculate_tour_cost(new_tour)
                if new_cost < best_cost:
                    best_tour, best_cost = new_tour[:], new_cost
                    improved = True
    return best_tour

def shake(tour):
    new_tour = tour[1:-1]  # Remove depot from beginning and end
    random.shuffle(new_tour)
    return [0] + new_tour + [0]

def gvns(k, max_iter=100):
    best_tour = generate_initial_solution()
    best_cost = calculate_tour_cost(best_tour)
    
    for _ in range(max_iter):
        current_tour = shake(best_tour)
        current_tour = local_search(current_tour)
        current_cost = calculate_tour_cost(current_tour)
        
        if current_cost < best_cost:
            best_tour, best_cost = current_tour[:], current_cost
            
    return best_tour, best_cost

# Solving the problem
best_tour, best_cost = gvns(4)
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))