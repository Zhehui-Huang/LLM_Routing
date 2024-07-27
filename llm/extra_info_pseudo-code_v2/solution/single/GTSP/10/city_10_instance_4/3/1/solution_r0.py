from math import sqrt
import random

# City positions
depot = (79, 15)
cities = [(79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), 
         (20, 99), (66, 62)]

# City groups
city_groups = [[1, 4], [2, 6], [7], [5], [9], [8], [3]]  # groups consist of indices in the cities' order

# Calculate Euclidean distance
def distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate an initial tour by selecting one city from each group and adding the depot at the beginning and end
def initial_tour():
    tour = [depot]
    for group in city_groups:
        chosen_city = cities[random.choice(group) - 1]
        tour.append(chosen_city)
    tour.append(depot)
    return tour

# Compute cost of the tour
def compute_total_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i + 1])
    return total_cost

# Heuristic for selecting one city from each group (we randomly pick one but this can be improved with a smarter heuristic)
def select_cities():
    return [random.choice(group) for group in city_groups]

# Helper function to convert city indices to coordinates, adding depot at start/end
def indices_to_coordinates(city_indices):
    tour = [depot] + [cities[index - 1] for index in city_indices] + [depot]
    return tour

# Main GLNS-like function to find best tour
def find_best_tour(num_trials, num_iterations):
    best_tour = None
    best_cost = float('inf')
    
    for _ in range(num_trials):
        city_indices = select_cities()
        current_tour = indices_to_coordinates(city_indices)
        current_cost = compute_total_cost(current_tour)
        
        for _ in range(num_iterations):
            new_city_indices = select_cities()
            new_tour = indices_to_coordinates(new_city_indices)
            new_cost = compute_total_cost(new_tour)
            
            if new_cost < current_cost:
                current_tour = new_tour
                current_cost = new_cost
                if current_cost < best_cost:
                    best_tour = current_tour
                    best_cost = current_cost
    
    return best_tour, best_cost

# Run the function with a certain number of trials and iterations
best_tour, best_cost = find_best_tour(num_trials=100, num_summary_iterations=100)

# Convert the best tour's coordinates back to indices for output
best_tour_indices = [0]  # depot start
for city in best_tour[1:-1]:
    index = cities.index(city) + 1
    best_tour_indices.append(index)

best_tour_indices.append(0)  # depot end

# Print the results
print("Tour:", best_tour_indices)
print("Total travel cost:", round(best_cost, 2))