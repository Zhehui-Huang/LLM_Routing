import math
from itertools import permutations

# City coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Greedy function to pick 9 additional cities based on their proximity to city 0 (depot)
def greedy_pick_cities(start, num_cities, total_cities):
    remaining_cities = set(range(total_cities)) - {start}
    tour = [start]
    
    while len(tour) < num_cities:
        nearest_city = min(remaining_cities, key=lambda x: euclidean_distance(tour[-1], x))
        tour.append(nearest_city)
        remaining_cities.remove(nearest_city)
    
    return tour

# Local search to refine the solution
def two_opt_swap(tour):
    best_distance = calculate_tour_length(tour)
    best_tour = tour[:]
    improved = True

    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1:
                    continue
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                new_distance = calculate_tour_length(new_tour)
                if new_distance < best_distance:
                    best_distance = new_distance
                    best_tour = new_tour
                    improved = True
        tour = best_tour
    
    return tour, best_distance

# Function to calculate the total tour length
def calculate_tour_length(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Select initial 10 cities including the depot
initial_tour = greedy_pick_cities(0, 10, len(cities))
initial_tour.append(0)  # To make it a round trip
final_tour, total_cost = two_opt_swap(initial_tour)

print("Tour:", final_tour)
print("Total travel cost:", total_cost)