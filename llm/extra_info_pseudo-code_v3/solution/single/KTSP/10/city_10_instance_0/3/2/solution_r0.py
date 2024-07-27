import math
import random

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def generate_initial_solution(cities):
    tour = [0]  # Start with the depot city
    available_cities = list(range(1, len(cities)))
    random.shuffle(available_cities)
    tour += available_cities[:3]  # Pick 3 other cities at random
    tour.append(0)  # End at the depot city
    return tour

def calculate_total_distance(tour, distances):
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += distances[tour[i]][tour[i+1]]
    return total_dist

def shake(tour):
    # Randomly swap two cities in the tour (not including the depot city 0)
    city1 = random.randint(1, 3)
    city2 = random.randint(1, 3)
    while city1 == city2:
        city2 = random.randint(1, 3)
    new_tour = tour[:]
    new_tour[city1], new_tour[city2] = new_tour[city2], new_tour[city1]
    return new_tour

def local_search(tour, distances):
    improved = True
    while improved:
        improved = False
        best_tour = tour[:]
        best_distance = calculate_total_distance(tour, distances)
        for i in range(1, 4):
            for j in range(i + 1, 4):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # Swap two cities
                new_distance = calculate_total_distance(new_tour, distances)
                if new_distance < best_distance:
                    best_tour = new_tour[:]
                    best_distance = new_distance
                    improved = True
        tour = best_tour
    return tour

def GVNS_algorithm(cities, nrst=1000):
    distances = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]
    best_solution = generate_initial_solution(cities)
    best_tour_cost = calculate_total_distance(best_solution, distances)
    
    for _ in range(nrst):
        current_solution = generate_initial_solution(cities)
        while True:
            current_solution_shaken = shake(current_solution)
            improved_solution = local_search(current_solution_shaken, distances)
            improved_cost = calculate_total_distance(improved_solution, distances)
            if improved_cost < best_tour_cost:
                best_solution = improved_solution
                best_tour_cost = improved_cost
                current_solution = improved_solution
            else:
                break

    return best_solution, best_tour_cost

# City coordinates
cities = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)]
best_tour, best_cost = GVNS_algorithm(cities)
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost}")