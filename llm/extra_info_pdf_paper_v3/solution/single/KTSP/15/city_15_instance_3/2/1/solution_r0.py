import math
import itertools

# City coordinates as given
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73), 
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all possible subsets of size k-1 from the given cities excluding the depot city
def get_city_subsets(cities, k):
    city_list = list(cities.keys())
    city_list.remove(0)  # removing the depot city
    return list(itertools.combinations(city_list, k-1))

# Function to calculate the cost of a tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i + 1])
    return total_cost

# Nearest neighbor heuristic to form an initial tour
def nearest_neighbor_tour(subset):
    current_city = 0
    tour = [current_city]
    remaining_cities = list(subset)
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda x: euclidean_distance(current_city, x))
        remaining_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city
    tour.append(0)  # return to depot
    return tour

# 2-opt optimization to improve a given tour
def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if tour[i - 1] != 0 or j + 1 != len(tour) - 1:  # Avoid breaking the return to the depot
                    new_tour = tour[:i] + tour[i:j + 1][::-1] + tour[j + 1:]
                    if calculate_tour_cost(new_tour) < calculate_tour_cost(tour):
                        tour = new_tour
                        improved = True
    return tour

# Main function to find the best tour with given constraints
def find_best_tour(cities, k):
    best_tour = None
    best_cost = float('inf')
    for subset in get_city_subsets(cities, k):
        subset = (0,) + subset  # add the depot to the subset
        tour = nearest_neighbor_tour(subset)
        optimized_tour = two_opt(tour)
        cost = calculate_tour_cost(optimized_tour)
        if cost < best_cost:
            best_cost = cost
            best_tour = optimized_tour
    return best_tour, best_cost

k = 10  # including the depot city
best_tour, best_cost = find_best_tour(cities, k)

print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))