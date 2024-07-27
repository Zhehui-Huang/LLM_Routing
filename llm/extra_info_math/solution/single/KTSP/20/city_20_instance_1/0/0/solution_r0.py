import math
import itertools

# Cities' coordinates
cities = [(14, 77), (34, 20), (19, 38), (14, 91), (68, 98), 
          (45, 84), (4, 56), (54, 82), (37, 28), (27, 45), 
          (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), 
          (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)]

# Calculate Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Generate all subsets of cities of size 7
def generate_city_subsets():
    return [list(comb) for comb in itertools.combinations(range(1, 20), 6)]

# Calculate the total distance of the tour
def calculate_tour_distance(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Find a tour by using a simple greedy heuristic: always go to the nearest unvisited city
def nearest_neighbour_tour(start, cities_subset):
    unvisited = cities_subset[:]
    tour = [start]
    current_city = start
    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(current_city, x))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    tour.append(start)  # return to start
    return tour

# 2-opt optimization to improve the initial tour
def two_opt_optimization(tour):
    best_tour = tour
    best_distance = calculate_tour_distance(tour)
    
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best_tour) - 2):
            for j in range(i + 1, len(best_tour) - 1):
                new_tour = best_tour[:]
                new_tour[i:j+1] = reversed(new_tour[i:j+1])
                
                new_distance = calculate_tour_distance(new_tour)
                if new_distance < best_distance:
                    best_tour = new_tour
                    best_distance = new_distance
                    improved = True
    return best_tour

# Main function to find the optimal tour
def find_optimal_tour():
    best_overall_distance = float('inf')
    best_overall_tour = None

    for subset in generate_city_subsets():
        full_subset = [0] + subset  # including the depot city
        initial_tour = nearest_neighbour_tour(0, full_subset)
        optimized_tour = two_opt_optimization(initial_tour)
        tour_distance = calculate_tour_distance(optimized_tour)
        
        if tour_distance < best_overall_distance:
            best_overall_distance = tour_distance
            best_overall_tour = optimized_tour
    
    return best_overall_tour, best_overall_distance

# Execute the function and print results
optimal_tour, optimal_distance = find_optimal_tour()
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_distance:.2f}")