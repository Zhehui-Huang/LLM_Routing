import math
import random

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_distance(tour, cities):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))

def generate_initial_tour(num_cities):
    tour = list(range(1, num_cities))
    random.shuffle(tour)
    return [0] + tour + [0]  # start and end at the depot city

def two_opt(tour, cities):
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # Consecutive cities
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if total_distance(new_tour, cities) < total_distance(tour, cities):
                    tour = new_tour
                    improvement = True
                    break
            if improvement:
                break
    return tour

# Define cities as points
cities = {
    0: (84, 67), 
    1: (74, 40), 
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Initialize and solve TSP
num_cities = len(cities)
initial_tour = generate_initial_tour(num_cities)
optimized_tour = two_opt(initial_tour, cities)
total_cost = total_distance(optimized_tour, cities)

# Output the results
print("Tour:", optimized_tour)
print("Total travel cost:", total_cost)